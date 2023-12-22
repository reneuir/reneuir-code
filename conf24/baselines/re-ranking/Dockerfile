FROM ubuntu:22.04

# Install dependencies
RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y python3 python3-pip python-is-python3 openjdk-11-jdk wget \
	&& pip3 install jupyter ir_datasets tira>=0.0.89 \
	&& rm -Rf /var/cache/apt \
	&& rm -Rf /root/.cache/pip

ADD baseline_re_ranking.py /code/baseline_re_ranking.py

ENTRYPOINT [ "python3", "/code/baseline_re_ranking.py" ]

