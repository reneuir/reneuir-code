#!/usr/bin/env python3
import json
import gzip
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Build an index')
    parser.add_argument('--input', type=str, help='The input directory.', required=True)
    parser.add_argument('--index', type=str, help='The index.', required=True)
    parser.add_argument('--output', type=str, help='The index will be stored in this directory.', required=True)
    
    return parser.parse_args()

def create_run(input_directory, index_directory, output_directory):
    """
    Creates a pseudo run file that just lists the first 5 document ids per query.
    """
    first_doc_ids = gzip.open(index_directory + '/pseudo_index.jsonl.gz', 'rt').readlines()[:5]

    with open(input_directory + '/queries.jsonl') as queries, open(output_directory + '/run.txt', 'w+') as run:
        for query in queries:
            query = json.loads(query)
        
            for rank, doc_id in zip(range(1, 6), first_doc_ids):
                run.write(f'{query["qid"]} Q0 {doc_id.strip()} {rank} {10-rank} my-system\n')

    print('Done: Run stored.')

if __name__ == '__main__':
    args = parse_args()
    create_run(args.input, args.index, args.output)
