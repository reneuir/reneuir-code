#!/usr/bin/env python3
#export IR_DATASETS_HOME=/mnt/ceph/tira/state/ir_datasets/
import ir_datasets
import pandas as pd
from trectools import TrecRun, TrecPoolMaker
from glob import glob
from tqdm import tqdm
import random

queries = {
    'trec-dl-2019': {i.query_id: i.default_text() for i in ir_datasets.load("msmarco-passage/trec-dl-2019/judged").queries_iter()},
    'trec-dl-2020': {i.query_id: i.default_text() for i in ir_datasets.load("msmarco-passage/trec-dl-2020/judged").queries_iter()}
}

docsstore = ir_datasets.load("msmarco-passage").docs_store()

def all_runs(track):
    runs = []
    for r in tqdm(glob(f'runs/{track}/*'), f'Parse runs from {track}'):
        runs += [TrecRun(r)]
    return runs

ret = {}
for track in queries:
    runs = all_runs(track)
    ret[track] = {}
    for pool_size in tqdm([5, 10, 20, 50, 100, 1000], 'Pool sizes'):
        pool = TrecPoolMaker().make_pool(runs, strategy="topX", topX=pool_size).pool
        queries_pool = list(set([i for i in pool.keys() if i in queries[track]]))
        ret[track][pool_size] = {i: list(pool[i]) for i in pool.keys() if i in queries_pool}

json.dumps(ret, open('document-dimensions-pool.json', 'w'))

