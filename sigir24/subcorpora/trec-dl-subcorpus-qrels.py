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
    with open(f'{depth}.qrels', 'w') as f:

        for qrel in tqdm(ir_datasets.load("msmarco-passage/trec-dl-2019").qrels_iter()):
            if qrel.doc_id in docs:
                f.write(f'{qrel.query_id} 0 {qrel.doc_id} {qrel.relevance}\n')

        for qrel in tqdm(ir_datasets.load("msmarco-passage/trec-dl-2020").qrels_iter()):
            if qrel.doc_id in docs:
                f.write(f'{qrel.query_id} 0 {qrel.doc_id} {qrel.relevance}\n')

