FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

# Smaller image, in the jupyter notebooks, we only use the SetwiseLlmRanker at the moment (i.e., first stage retrieval not needed)
RUN pip3 install --no-deps pyserini ir-datasets

RUN pip3 install openai tiktoken accelerate transformers llm-rankers sentencepiece tira jupyter runnb

ARG MODEL_NAME
ENV MODEL=$MODEL_NAME
ADD run-notebook.py re-rank-with-llm-rankers.ipynb /app/

ENTRYPOINT [ "/app/run-notebook.py", "--notebook", "/app/re-rank-with-llm-rankers.ipynb" ]

