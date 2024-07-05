#docker build -t plaid-x .
FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

RUN apt-get update \
	&& apt-get install -y build-essential

RUN pip3 install transformers tira jupyter runnb PLAID-X

#ADD run-notebook.py plaid-indexing.ipynb /app/

