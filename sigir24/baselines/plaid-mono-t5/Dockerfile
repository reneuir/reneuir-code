# docker build -t plaid-mono-t5 .
FROM docker.io/webis/ir-benchmarks-submissions:tira-ir-starter-pygaggle-0-0-1-monot5-3b-msmarco-tira-docker-software-id-brown-tree

RUN pip3 uninstall -y tira \
	&& pip3 install tira \
	&& pip3 install --no-deps ir-datasets

ADD pipeline.sh rerank-file-from-plaid-x.py /

ENTRYPOINT [ "/pipeline.sh", "$inputDataset", "$outputDir" ]
