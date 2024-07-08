#!/usr/bin/env bash

INPUT_RUN=$(tira-cli download --dataset $1 --approach reneuir-2024/reneuir-baselines/plaid-x-retrieval)

/rerank-file-from-plaid-x.py --output /tmp/ --input-dataset $1 --input-run ${INPUT_RUN}/run.txt --top-k 1200

zcat /tmp/rerank.jsonl.gz |head -10
cp /tmp/rerank.jsonl.gz ${inputDataset}/rerank.jsonl.gz

/reranking.py --input /tmp --output $2

