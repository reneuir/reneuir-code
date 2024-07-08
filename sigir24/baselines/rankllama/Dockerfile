FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-devel

RUN apt-get update \
	&& apt-get install -y git \
	&& pip3 install flash-attn accelerate transformers peft sentencepiece tira jupyter runnb protobuf \
	&& pip3 install --no-deps ir-datasets

ADD re-rank-with-rankllama.ipynb run-notebook.py /app/

ENTRYPOINT [ "/app/run-notebook.py", "--notebook", "/app/re-rank-with-rankllama.ipynb", "--offline", "True" ]

