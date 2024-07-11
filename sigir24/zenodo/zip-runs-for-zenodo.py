#!/usr/bin/env python3
from tira.profiling_integration import ProfilingIntegration
from pathlib import Path
from tqdm import tqdm
import pandas as pd
import json
import zipfile

def _run_dir(user_id, dataset_id, run_id):
    return Path(f'/mnt/ceph/tira/data/runs/{dataset_id}/{user_id}/{run_id}/')

def ensure_run_did_run_on_gammaweb09(user_id, dataset_id, run_id):
    run_dir = _run_dir(user_id, dataset_id, run_id) / 'profiling.zip'
    cpuinfo = ProfilingIntegration(None)._read_file_from_profiling_zip(run_dir, 'cpuinfo')
    nvidia_smi = ProfilingIntegration(None)._read_file_from_profiling_zip(run_dir, 'nvidia-smi.out')

    if 'AMD EPYC 7F72 24-Core Processor' not in cpuinfo:
        raise ValueError('Did not run on gammaweb09: ', run_dir)

    if 'NVIDIA A100-SXM4-40GB' not in nvidia_smi:
        raise ValueError('Did not run on gammaweb09: ', run_dir)


def zip_runs(name, paths_to_be_zipped):
    """ Copied from "from tira.views import zip_run, zip_runs" to run this without the tira server dependencies """
    
    zipped = Path(f"/mnt/ceph/storage/web/files/data-in-production/data-research/tira-zenodo-dump-preparation/reneuir-2024/runs/{name}.zip")
    if zipped.exists():
        return

    with zipfile.ZipFile(zipped, "w", zipfile.ZIP_DEFLATED) as zipf:
        for path_to_be_zipped in paths_to_be_zipped:
            path_to_be_zipped = Path(path_to_be_zipped)
            for f in path_to_be_zipped.rglob('*'):
                zipf.write(f, arcname=f.relative_to(path_to_be_zipped.parent))

    return zipped

def aggregation_of_run(user_id, dataset_id, run_id):
    run_dir = _run_dir(user_id, dataset_id, run_id)
    profiling = ProfilingIntegration(None).from_local_run_output(run_dir)

    elapsed_time = profiling[-1]
    assert elapsed_time['key'] == 'elapsed_time'
    elapsed_time = elapsed_time['value']
    rss = [i['value'] for i in profiling if i['key'] == 'ps_vsz']
    gpu_memory_used = [int(i['value'].split()[0]) for i in profiling if i['key'] == 'gpu_memory_used']
    gpu_utilization = [int(i['value'].split()[0]) for i in profiling if i['key'] == 'gpu_utilization']
    cpu_utilization = [i['value'] for i in profiling if i['key'] == 'ps_cpu']

    return {
        'Elapsed Time': elapsed_time,
        'CPU Utilization (Max)': max(cpu_utilization),
        'RSS (MAX)': max(rss),
        'GPU Memory (Max)': max(gpu_memory_used),
        'GPU Utilization (Max)': max(gpu_utilization),
    }


if __name__ == '__main__':
    runs = json.load(open('runs.json'))
    ret = []
    
    groups_for_archival = {}
    
    for i in runs:
        task, user_id, approach = i.split('/')
        group = runs[i]['class'] if 'class' in runs[i] else f'{user_id}-{approach}'.lower().replace(' ', '-').replace('(', '').replace(')', '')
        
        if group not in groups_for_archival:
            groups_for_archival[group] = {}
        
        for dataset_id, run_id in runs[i]['runs'].items():
            assert run_id not in groups_for_archival[group]
            groups_for_archival[group][run_id] = _run_dir(user_id, dataset_id, run_id)
            ensure_run_did_run_on_gammaweb09(user_id, dataset_id, run_id)
            tmp = {'approach': i, 'dataset': dataset_id, 'run_id': run_id}
            tmp.update(aggregation_of_run(user_id, dataset_id, run_id))
            ret += [tmp]

    pd.DataFrame(ret).to_json('aggregated-profiling.jsonl', lines=True, orient='records')
    
    for archive_group in tqdm(groups_for_archival.keys(), 'Zip runs'):
        runs_to_zip = sorted(list(groups_for_archival[archive_group].values()))
        zip_runs(archive_group, runs_to_zip)

