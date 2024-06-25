#!/usr/bin/env python3
#export IR_DATASETS_HOME=/mnt/ceph/tira/state/ir_datasets/
import ir_datasets
from trectools import TrecRun
from tqdm import tqdm
import gzip
import json

queries = {i.query_id: i.default_text() for i in ir_datasets.load("msmarco-passage/dev/small").queries_iter()}
docsstore = ir_datasets.load("msmarco-passage").docs_store()

run = TrecRun('/mnt/ceph/storage/web/files/data-in-progress/data-research/web-search/reneuir-24/msmarco-dev-dataset/msmarco-passage-dev-small.run').run_data

with gzip.open('all-rerank.jsonl.gz', 'wt') as f:
    for _, i in tqdm(run.iterrows(), total=len(run)):
        f.write(json.dumps({"qid": str(i['query']), "query": queries[str(i['query'])], "original_query": {}, "docno": i['docid'], "text": docsstore.get(i['docid']).default_text(), "original_document": {}, "rank": i['rank'], "score": i['score']}) + '\n')

# Todo: Analogous for 1000 queries
run_1000 = Y

# todo: analogous for 100 queries
run_100 = y

