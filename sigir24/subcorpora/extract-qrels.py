#!/usr/bin/env python3
from os import environ
import pandas as pd
import ir_datasets
from tqdm import tqdm

src_file = (environ['PWD'] + '/rerank.jsonl.gz').replace('/training-datasets-truth/', '/training-datasets/')
print(src_file)
df = pd.read_json(src_file, lines=True, orient='records')
qids = set(df['qid'].astype(str).unique())

with open('qrels.txt', 'w') as f:
    for qrel in tqdm(ir_datasets.load("msmarco-passage/dev/small").qrels_iter()):
        if qrel.query_id in qids:
            f.write(f'{qrel.query_id} 0 {qrel.doc_id} {qrel.relevance}\n')

print(len(qids))

