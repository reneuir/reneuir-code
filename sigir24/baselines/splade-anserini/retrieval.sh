#!/usr/bin/env bash

set -e

DATASET="$1"
shift
ENCODED_CORPUS_DIR="$(tira-cli download --dataset ${DATASET} --approach reneuir-2024/reneuir-baselines/splade-anserini-encoding)"
INDEX_DIR="$(tira-cli download --dataset ${DATASET} --approach reneuir-2024/reneuir-baselines/splade-anserini-index)/index"


java -cp /jars/anserini-0.36.1-fatjar.jar \
	io.anserini.search.SearchCollection \
	-index ${INDEX_DIR} \
	-topics ${ENCODED_CORPUS_DIR}/queries_anserini.tsv \
	-topicReader TsvInt \
	-impact -pretokenized \
	${@}

/backtranslation-of-ids.py ${ENCODED_CORPUS_DIR} ${@}

