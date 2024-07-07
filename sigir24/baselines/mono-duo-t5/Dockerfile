# docker build -t mono-duo-t5 .
FROM webis/ir-benchmarks-submissions:tira-ir-starter-duot5-0-0-1-3b-msmarco-tira-docker-software-id-courtly-spline

RUN pip3 uninstall -y tira \
	pip3 uninstall -y ir_datasets \
	&& pip3 install tira ir_datasets \
	&& rm -R /workspace/

ADD reranking.py /reranking.py
