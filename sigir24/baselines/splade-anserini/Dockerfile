#docker build -t anserini-splade .
FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

RUN apt-get update \
	&& apt-get install -y git \
	&& git clone https://github.com/naver/splade.git /splade \
	&& cd /splade \
	&& conda env create -f conda_splade_env.yml

ENV PYTHONPATH=/splade:.
ENV HF_HUB_OFFLINE=1
ENV OFFLINE=True

RUN cd /splade \
	&& /opt/conda/envs/splade/bin/python3 \
	-m splade.create_anserini \
	init_dict.model_type_or_dir=naver/splade-cocondenser-ensembledistil \
	config.pretrained_no_yamlconfig=true \
	config.index_dir=/tmp/tmp-index \
	config.out_dir=/tmp/tmp-out \
	+quantization_factor_document=100   +quantization_factor_query=100 \
	&& pip3 install tira \
	&& pip3 install --no-deps ir-datasets

ADD run-anserini-splade.sh transform-data.py /

ENTRYPOINT [ "bash", "-c", "'cd / && ./run-anserini-splade.sh $inputDataset $outputDir'" ]
