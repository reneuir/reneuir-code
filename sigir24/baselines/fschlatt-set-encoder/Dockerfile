FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install \
    transformers \
    ir-datasets \
    ir-measures \
    lightning \
    pandas \
    'jsonargparse[signatures]>=4.27.7' \
    git+https://github.com/webis-de/lightning-ir.git \
    && pip cache purge

RUN git clone https://github.com/webis-de/set-encoder /workspace/set-encoder

ADD run.sh /workspace/run.sh
ADD config.yaml /config/config.yaml
ENV PYTHONPATH=/workspace/set-encoder

ARG MODEL_NAME
ENV MODEL=$MODEL_NAME
ENV CONFIG_DIR=/config
ENV HF_HUB_OFFLINE=1
ENV OFFLINE=True


ENTRYPOINT [ "run.sh" ]
