#!/usr/bin/env python3
import pandas as pd
import json
import argparse
import pandas as pd
import os

parser = argparse.ArgumentParser()
parser.add_argument('mapping_dir')
parser.add_argument('-output', required=True)
args = parser.parse_args()

query_ids = json.load(open(f'{args.mapping_dir}/query-ids.json'))
document_ids = json.load(open(f'{args.mapping_dir}/document-ids.json'))

run = pd.read_csv(args.output, sep="\\s+", names=["query", "q0", "docid", "rank", "score", "system"], dtype={'query': int, 'docid': int})

os.remove(args.output)

run['query'] = run['query'].apply(lambda i: query_ids[i])
run['docid'] = run['docid'].apply(lambda i: document_ids[i])

run.to_csv(args.output, sep=" ", header=False, index=False)
