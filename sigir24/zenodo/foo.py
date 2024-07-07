#!/usr/bin/env python3
from tira.profiling_integration import ProfilingIntegration
from pathlib import Path
import pandas as pd
import json

def ensure_run_did_run_on_gammaweb09(user_id, dataset_id, run_id):
    run_dir = Path(f'/mnt/ceph/tira/data/runs/{dataset_id}/{user_id}/{run_id}/profiling.zip')
    cpuinfo = ProfilingIntegration(None)._read_file_from_profiling_zip(run_dir, 'cpuinfo')
    nvidia_smi = ProfilingIntegration(None)._read_file_from_profiling_zip(run_dir, 'nvidia-smi.out')

    if 'AMD EPYC 7F72 24-Core Processor' not in cpuinfo:
        raise ValueError('Did not run on gammaweb09: ', run_dir)

    if 'NVIDIA A100-SXM4-40GB' not in nvidia_smi:
        raise ValueError('Did not run on gammaweb09: ', run_dir)


def aggregation_of_run(user_id, dataset_id, run_id):
    run_dir = Path(f'/mnt/ceph/tira/data/runs/{dataset_id}/{user_id}/{run_id}/')
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
    for i in runs:
        task, user_id, approach = i.split('/')
        for dataset_id, run_id in runs[i]['runs'].items():
            ensure_run_did_run_on_gammaweb09(user_id, dataset_id, run_id)
            tmp = {'approach': i, 'dataset': dataset_id, 'run_id': run_id}
            tmp.update(aggregation_of_run(user_id, dataset_id, run_id))
            ret += [tmp]

    pd.DataFrame(ret).to_json('aggregated-profiling.jsonl', lines=True, orient='records')

