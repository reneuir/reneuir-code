#!/usr/bin/env python3
# Load a patched ir_datasets that loads the injected data inside the TIRA sandbox
from tira.third_party_integrations import load_rerank_data, persist_and_normalize_run
from pathlib import Path
import pandas as pd

def score_query_document_pair(query, document_text, score_of_previous_stage):
    # Our baseline re-ranker just emits 1 + the score of the previous ranker.
    return 1 + score_of_previous_stage

if __name__ == '__main__':
    # In the TIRA sandbox, this is the injected re-ranking dataset, injected via the environment variable TIRA_INPUT_DIRECTORY
    re_rank_dataset = load_rerank_data(default='workshop-on-open-web-search/re-ranking-20231027-training')

    # Alternatively, you could use the scored docs of ir_datasets, e.g.:
    # from tira.third_party_integrations import ir_dataset
    # dataset = ir_datasets.load(default='workshop-on-open-web-search/document-processing-20231027-training')

    run = []

    for _, i in re_rank_dataset.iterrows():
        run += [{'qid': i['qid'], 'docno': i['docno'], 'score': score_query_document_pair(i['query'], i['text'], i['score'])}]
    
    run = pd.DataFrame(run)
    
    # Re-rankers are expected to produce a TREC-style run.txt file in the output directory.
    persist_and_normalize_run(run, 'my-system-name', default_output='./run.txt')
    
    # You can pass additional arguments to your program, e.g., via argparse, to modify the behaviour of your program.
    
