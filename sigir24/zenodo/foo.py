from tira.profiling_integration import ProfilingIntegration
from pathlib import Path
import json

def ensure_run_did_run_on_gammaweb09(user_id, dataset_id, run_id):
    run_dir = Path(f'/mnt/ceph/tira/data/runs/{dataset_id}/{user_id}/{run_id}/'
    print(ProfilingIntegration()._read_file_from_profiling_zip(run_dir, 'cpu_info'))

if __name__ == '__main__':
    runs = json.load(open('runs.json'))
    for i in runs:
        task, user_id, approach = i.split('/')
        for dataset_id, run_id in runs[i]['runs'].items():
            ensure_run_did_run_on_gammaweb09(user_id, dataset_id, run_id)

