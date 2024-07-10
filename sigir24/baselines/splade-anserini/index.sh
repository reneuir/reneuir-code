#!/usr/bin/env bash

set -e

DATASET="$1"
shift
INPUT_DIR=$(tira-cli download --dataset ${DATASET})
ENCODED_CORPUS_DIR="$(tira-cli download --dataset ${DATASET} --approach reneuir-2024/reneuir-baselines/splade-anserini-encoding)"

ls -lha ${ENCODED_CORPUS_DIR}

java -cp /jars/anserini-0.36.1-fatjar.jar \
	io.anserini.index.IndexCollection \
	-collection JsonVectorCollection \
	-input ${ENCODED_CORPUS_DIR} \
	-generator DefaultLuceneDocumentGenerator \
	-impact -pretokenized \
	${@}

