#!/usr/bin/env python3
import json

approach_to_telemetry = {}
runs = json.load(open('runs.json'))

with open('single-stage-telemetry.jsonl', 'r') as f:
    for l in f:
        l = json.loads(l)
        if l['approach'] not in approach_to_telemetry:
            approach_to_telemetry[l['approach']] = {}

        assert l['dataset'] not in approach_to_telemetry[l['approach']]
        approach_to_telemetry[l['approach']][l['dataset']] = l

def aggregate_previous_stages(i, dataset_id):
    prev = sorted(list(set(all_previous_stages(i))))
    
    ret = {'Elapsed Time': [], 'CPU Utilization (Max)': [], 'RSS (MAX)': [], 'GPU Memory (Max)': [], 'GPU Utilization (Max)': []}
    for p in prev:
        for k in ret:
            ret[k] += [approach_to_telemetry[p][dataset_id][k]]
    
    return {
        'Elapsed Time': sum(ret['Elapsed Time']),
        'CPU Utilization (Max)': max(ret['CPU Utilization (Max)']),
        'RSS (MAX)': max(ret['RSS (MAX)']),
        'GPU Memory (Max)': max(ret['GPU Memory (Max)']),
        'GPU Utilization (Max)': max(ret['GPU Utilization (Max)']),   
    }

def all_previous_stages(i):
    if i and 'previous-stage' in runs[i] and len(runs[i]['previous-stage']) > 0:
        ret = []
        for p in runs[i]['previous-stage']:
            ret += all_previous_stages(p)
        
        return [i] + runs[i]['previous-stage'] + ret
    else:
        return [i]

ret = {}
with open('single-stage-telemetry.jsonl', 'r') as f:
    dataset_id = 'dl-top-1000-docs-20240701-training'
    for l in f:
        l = json.loads(l)
        if l['dataset'] != dataset_id:
            continue
    assert l['approach'] not in ret
    tmp = {'approach': l['approach'], 'dataset': l['dataset'], 'run_id': l['run_id']}
    tmp.update(aggregate_previous_stages(tmp['approach'], dataset_id))
    ret[tmp['approach']]  = tmp

json.dump(ret, open('../post-hoc-notebooks/aggregated-telemetry.json', 'w'))

