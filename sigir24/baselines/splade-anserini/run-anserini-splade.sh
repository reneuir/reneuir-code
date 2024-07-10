#!/usr/bin/env bash

#stop on first error
set -e 

mkdir -p /tmp/corpus
mkdir -p /tmp/queries

./transform-data.py /tmp/corpus/raw.tsv /tmp/queries/raw.tsv --dataset-id $1

/opt/conda/envs/splade/bin/python3 \
	-m splade.create_anserini \
	init_dict.model_type_or_dir=naver/splade-cocondenser-ensembledistil \
	config.pretrained_no_yamlconfig=true \
	config.index_dir=/tmp/tmp-index \
	config.out_dir=$2 \
	+quantization_factor_document=100 \
	+quantization_factor_query=100 \
	data.COLLECTION_PATH=/tmp/corpus \
	data.Q_COLLECTION_PATH=[/tmp/queries]

mv /tmp/corpus/raw.tsv-ids.json $2/document-ids.json
mv /tmp/queries/raw.tsv-ids.json $2/query-ids.json

