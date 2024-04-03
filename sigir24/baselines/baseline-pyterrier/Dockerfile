FROM ubuntu:22.04

# Install dependencies
RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y python3 python3-pip python-is-python3 openjdk-11-jdk wget \
	&& pip3 install jupyter ir_datasets tira>=0.0.112 python-terrier \
	&& python3 -c 'from tira.third_party_integrations import ensure_pyterrier_is_loaded, persist_and_normalize_run; ensure_pyterrier_is_loaded()' \
	&& rm -Rf /var/cache/apt \
	&& rm -Rf /root/.cache/pip

ADD *.py /
