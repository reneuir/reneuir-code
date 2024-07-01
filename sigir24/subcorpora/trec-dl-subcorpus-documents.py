#!/usr/bin/env python3
#export IR_DATASETS_HOME=/mnt/ceph/tira/state/ir_datasets/
import ir_datasets
import pandas as pd
from trectools import TrecRun, TrecPoolMaker
from glob import glob
from tqdm import tqdm
import random
import gzip
import json

docsstore = ir_datasets.load("msmarco-passage").docs_store()

for depth in [10, 100, 1000]:
    docs = set()
    for track in ['dl-2019', 'dl-2020']:
        pool = json.load(open(f'document-dimensions-pool-{depth}-trec-{track}.json'))
        for k, d in pool.items():
            docs.update(d)
    print(depth, len(docs))
    with gzip.open(f'{depth}.documents.jsonl.gz', 'wt') as f:
        for d in tqdm(docs, f'Depth {depth}'):
            d = docsstore.get(d)
            f.write(json.dumps({"docno": str(d), "text": d.default_text()}) + '\n')

