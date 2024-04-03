#!/usr/bin/env python3
import json
import gzip
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Build an index')
    parser.add_argument('-i', type=str, help='The input directory.', required=True)
    parser.add_argument('-o', type=str, help='The index will be stored in this directory.', required=True)
    
    return parser.parse_args()

def create_index(input_directory, output_directory):
    """
    Load the documents from the input directory and build a pseudo index, just a list of document ids.
    """
    with gzip.open(input_directory + '/documents.jsonl.gz', 'rt') as documents, gzip.open(output_directory + '/pseudo_index.jsonl.gz', 'wt') as f:
        for doc in documents:
            doc = json.loads(doc)
            f.write(doc['docno'] + '\n')
            
    print('Done: Index stored.')


if __name__ == '__main__':
    args = parse_args()
    create_index(args.i, args.o)
