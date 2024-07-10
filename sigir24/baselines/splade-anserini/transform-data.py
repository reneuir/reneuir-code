#!/usr/bin/env python3
import pandas as pd
import json
from tira.third_party_integrations import ir_datasets
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('output_docs_file')
parser.add_argument('output_queries_file')
parser.add_argument('--dataset-id', default='reneuir-2024/dl-top-10-docs-20240701-training')
args = parser.parse_args()

# the "from tira.third_party_integrations import ir_datasets" import patches "ir_datasets.load"
# so that it loads the dataset injected into the tira sandbox when executed within the sandbox.
# I.e., we only ensure that it runs on a minimal spot-check dataset here.
dataset = ir_datasets.load(args.dataset_id)

docs = []
doc_ids = []
doc_cnt = 0
for d in dataset.docs_iter():
    docs += [{'doc_id': doc_cnt, 'text': d.default_text()}]
    doc_cnt += 1
    doc_ids += [str(d.doc_id)]

print(f'Write {len(docs)} to {args.output_docs_file}.')
pd.DataFrame(docs).to_csv(args.output_docs_file, sep='\t', header=False, index=False)
json.dump(doc_ids, open(args.output_docs_file + '-ids.json', 'w+'))

queries = []
query_ids = []
queries_cnt = 0
for q in dataset.queries_iter():
    queries += [{'query_id': queries_cnt, 'text': q.default_text()}]
    queries_cnt += 1
    query_ids += [str(q.query_id)]

print(f'Write {len(queries)} to {args.output_queries_file}.')
pd.DataFrame(queries).to_csv(args.output_queries_file, sep='\t', header=False, index=False)
json.dump(query_ids, open(args.output_queries_file + '-ids.json', 'w+'))

