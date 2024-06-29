#!/usr/bin/env python3
#export IR_DATASETS_HOME=/mnt/ceph/tira/state/ir_datasets/
import ir_datasets
from trectools import TrecRun
import random
from tqdm import tqdm
import gzip
import json

def random_subset(t, size):
    """Size is also used as seed"""
    random.seed(size)
    t = [i for i in t]
    sorted(t)
    random.shuffle(t)
    return set(t[:size])

queries = {i.query_id: i.default_text() for i in ir_datasets.load("msmarco-passage/dev/small").queries_iter()}
docsstore = ir_datasets.load("msmarco-passage").docs_store()

run = TrecRun('/mnt/ceph/storage/web/files/data-in-progress/data-research/web-search/reneuir-24/msmarco-dev-dataset/msmarco-passage-dev-small.run').run_data

query_ids = list(run['query'].unique())
query_ids_1000 = random_subset(query_ids, 1000)
print('1000 subset:', list(query_ids_1000)[:5], ',size:', len(query_ids_1000))
query_ids_100 = random_subset(query_ids, 100)
print('100 subset:', list(query_ids_100)[:5], ',size:', len(query_ids_100))

def persist(i, f):
    f.write(json.dumps({"qid": str(i['query']), "query": queries[str(i['query'])], "original_query": {}, "docno": i['docid'], "text": docsstore.get(i['docid']).default_text(), "original_document": {}, "rank": i['rank'], "score": i['score']}) + '\n')


with gzip.open('all-rerank.jsonl.gz', 'wt') as f:
    for _, i in tqdm(run.iterrows(), total=len(run)):
        persist(i, f)

# Todo: Analogous for 1000 queries
run_1000 = run[run['query'].isin(query_ids_1000)]
with gzip.open('1000-rerank.jsonl.gz', 'wt') as f:
    for _, i in tqdm(run_1000.iterrows(), total=len(run_1000)):
        persist(i, f)



# todo: analogous for 100 queries
run_100 = run[run['query'].isin(query_ids_100)]
with gzip.open('100-rerank.jsonl.gz', 'wt') as f:
    for _, i in tqdm(run_100.iterrows(), total=len(run_100)):
        persist(i, f)

