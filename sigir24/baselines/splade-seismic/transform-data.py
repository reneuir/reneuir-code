#!/usr/bin/env python3
import pandas as pd
import json
from tira.third_party_integrations import ir_datasets
from huggingface_hub import snapshot_download
import argparse
from tqdm import tqdm
import  tarfile

parser = argparse.ArgumentParser()
parser.add_argument('output_file')
parser.add_argument('--type', choices=['query', 'document'], required=True)
parser.add_argument('--dataset-id', default='reneuir-2024/dl-top-10-docs-20240701-training')
parser.add_argument('--seismic-data-repo', default='tuskanny/seismic-msmarco-splade')
parser.add_argument('--quantized', action='store_true')

args = parser.parse_args()

dataset = ir_datasets.load(args.dataset_id)
data_repo = snapshot_download(repo_id=args.seismic_data_repo, repo_type="dataset", local_files_only=True)
ret = []

if args.type == 'query':
    allowed_query_ids = set([str(i.query_id) for i in dataset.queries_iter()])
    t = tarfile.open(data_repo + '/queries.tar.gz')
    for i in tqdm(t.extractfile('queries_anserini.tsv')):
        i = json.loads(i.decode('utf-8'))
        if str(i['id']) not in allowed_query_ids:
            continue
        if args.quantized:
            i['vector'] = {k:int(v*100) for k,v in i['vector'].items() if v >= 0.01}

        ret += [i]
else:
    allowed_document_ids = set([str(i.doc_id) for i in tqdm(dataset.docs_iter(), 'allowlist')])

    t = tarfile.open(data_repo + '/documents.tar.gz')
    for i in tqdm(t.extractfile('docs_anserini.jsonl'), 'filtering'):
        i = json.loads(i.decode('utf-8'))
        if str(i['id']) not in allowed_document_ids:
            continue

        if args.quantized:
            i['vector'] = {k:int(v*100) for k,v in i['vector'].items() if v >= 0.01}

        ret += [i]

with open(args.output_file, 'w') as f:
    for l in ret:
        f.write(json.dumps(l) + '\n')

