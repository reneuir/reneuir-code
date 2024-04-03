#!/usr/bin/env python3
import json
import gzip
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Build an index')
    parser.add_argument('-i', type=str, help='The input directory containint the rerank.jsonl.gz.', required=True)
    parser.add_argument('-o', type=str, help='The run file will be stored in this directory.', required=True)
    
    return parser.parse_args()

def score_query_document_pair(query, document_text, score_of_previous_stage):
    # Our baseline re-ranker just emits 1 + the score of the previous ranker.
    return 1 + score_of_previous_stage

if __name__ == '__main__':
    args = parse_args()

    with gzip.open(args.i + '/rerank.jsonl.gz', 'rt') as query_document_pairs, open(args.o + '/run.txt', 'w+') as run:
        for query_document_pair in query_document_pairs:
            query_document_pair = json.loads(query_document_pair)

            qid = query_document_pair['qid']
            docno = query_document_pair['docno']
            rank = query_document_pair['rank']
            # Our baseline re-ranker just emits 1 + the score of the previous ranker.
            score = query_document_pair['score'] + 1
            run.write(f'{qid} Q0 {docno} {rank} {score} my-system\n')

    print('Done: Run stored.')