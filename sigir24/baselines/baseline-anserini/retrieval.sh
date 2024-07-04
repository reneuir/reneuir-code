#!/usr/bin/env bash

DATASET="$1"
shift
INPUT_DIR=$(tira-cli download --dataset ${DATASET})
INDEX_DIR="$(tira-cli download --dataset ${DATASET} --approach reneuir-2024/reneuir-baselines/anserini-index)/index"

echo "Will use topics from ${INPUT_DIR}. Will use Index from ${INDEX_DIR}"

java -cp /jars/anserini-0.36.1-fatjar.jar \
    io.anserini.search.SearchCollection \
    -index ${INDEX_DIR} \
    -topics ${INPUT_DIR}/queries.xml \
    -topicField query \
    -topicReader Covid \
    ${@}