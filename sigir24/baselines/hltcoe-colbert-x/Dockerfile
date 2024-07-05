#docker build -t plaid-x .
FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-devel

RUN apt-get update \
	&& apt-get install -y build-essential git \
	&& conda install pytorch::faiss-gpu \
	&& pip3 install transformers tira jupyter runnb PLAID-X \
	&& python3 -c 'from colbert.indexing.codecs.residual import ResidualCodec; ResidualCodec.try_load_torch_extensions(True);' \
	&& rm -Rf /root/.cache/pip

RUN huggingface-cli download hltcoe/plaidx-large-eng-tdist-mt5xxl-engeng \
	&& huggingface-cli download xlm-roberta-large

ADD run-notebook.py plaid-x-indexing.ipynb /app/

RUN /app/run-notebook.py --notebook /app/plaid-x-indexing.ipynb \
	&& rm -Rf /tmp/index

RUN apt-get install -y vim

