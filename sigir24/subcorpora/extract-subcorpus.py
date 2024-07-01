#!/usr/bin/env python3
from os import environ
import gzip
import pandas as pd
import ir_datasets
from tqdm import tqdm
import json
from xml.sax.saxutils import escape

src_file = (environ['PWD'] + '/rerank.jsonl.gz')
print(src_file)
documents = {}
queries = {}
df = pd.read_json(src_file, lines=True, orient='records', dtype={'qid': str, 'docno': str})

for _, i in tqdm(df.iterrows()):
    queries[i['qid']] = i['query']
    documents[i['docno']] = i['text']

with gzip.open('documents.jsonl.gz', 'wt') as f:
    for docno, text in documents.items():
        f.write(json.dumps({'docno': docno, 'text': text}) + '\n')

with open('queries.jsonl', 'w') as f:
    for qid, query in queries.items():
        f.write(json.dumps({'qid': qid, 'query': query}) + '\n')

with open('queries.xml', 'w') as f:
    f.write('<topics>\n')
    for qid, query in queries.items():
        f.write(f' <topic number="{qid}">\n  <query>\n    {escape(query)}\n  </query>\n </topic>\n')
    f.write('</topics>')

