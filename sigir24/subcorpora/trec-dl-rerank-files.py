#!/usr/bin/env python3
#export IR_DATASETS_HOME=/mnt/ceph/tira/state/ir_datasets/
from trectools import TrecRun
from os import environ
import gzip
import pandas as pd
import ir_datasets
from tqdm import tqdm
import json

datasets = {
    'dl-top-10-docs-20240701-training': '2024-07-01-15-45-55',
    'dl-top-100-docs-20240701-training': '2024-07-01-15-46-44',
    'dl-top-1000-docs-20240701-training': '2024-07-01-15-47-04',
}

queries = {}
for ds in ["msmarco-passage/trec-dl-2019/judged", "msmarco-passage/trec-dl-2020/judged"]:
    for i in ir_datasets.load(ds).queries_iter():
        queries[i.query_id] = i.default_text()

docsstore = ir_datasets.load("msmarco-passage").docs_store()

for dataset, run_id in datasets.items():
    run = TrecRun(f'/mnt/ceph/tira/data/runs/{dataset}/tira-ir-starter/{run_id}/output/run.txt').run_data
    with gzip.open(f'{dataset}-rerank.jsonl.gz', 'wt') as f:
        for _, i in tqdm(list(run.iterrows()), dataset):
            f.write(json.dumps({"qid": str(i['query']), "query": queries[str(i['query'])], "original_query": {}, "docno": i['docid'], "text": docsstore.get(i['docid']).default_text(), "original_document": {}, "rank": i['rank'], "score": i['score']}) + '\n')

