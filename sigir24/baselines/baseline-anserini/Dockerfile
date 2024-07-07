#docker build -t mam10eks/anserini:0.0.1 .
FROM openjdk:24-slim

RUN mkdir /jars \
    && apt-get update \
    && apt-get install -y python3 python3-pip curl procps \
    && curl --output /jars/anserini-0.36.1-fatjar.jar https://repo1.maven.org/maven2/io/anserini/anserini/0.36.1/anserini-0.36.1-fatjar.jar \
    && pip3 install tira --break-system-packages \
    && rm -R /root/.cache/pip/

ADD io/anserini/collection/TirexJsonCollection.java /classes/io/anserini/collection/TirexJsonCollection.java
ADD retrieval.sh /

RUN cd /classes \
	&& javac -cp /jars/anserini-0.36.1-fatjar.jar io/anserini/collection/TirexJsonCollection.java
