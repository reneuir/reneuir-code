You can just start a devcontainer in this directory. In this case, your IDE (e.g., Visual Studio Code) handles the docker part (assuming you have docker installed).

If you want to develop without dev containers, you can, (1) build the Docker image (e.g., `docker build -t llm-rankers .`) and start a jupyter server (e.g., `docker run --rm -ti -v ${PWD}:/workspace --entrypoint jupyter -p 8888:8888 llm-rankers notebook --ip 0.0.0.0 --allow-root`).


# Submitted Variants

### meta-llama/Llama-2-7b-chat-hf

```
docker build -t llm-rankers-llama-2-7b-chat --build-arg MODEL_NAME=meta-llama/Llama-2-7b-chat-hf .
```

Test locally + upload to TIRA:
```
tira-run \
	--image llm-rankers-llama-2-7b-chat \
	--mount-hf-model meta-llama/Llama-2-7b-chat-hf \
	--input-dataset reneuir-2024/re-rank-spot-check-20240624-training
```

### lmsys/vicuna-13b-v1.5

```
docker build -t llm-rankers-vicuna-13b-v1.5 --build-arg MODEL_NAME=lmsys/vicuna-13b-v1.5 .
```

Test locally + upload to TIRA:
```
tira-run \
	--image llm-rankers-vicuna-13b-v1.5 \
	--mount-hf-model lmsys/vicuna-13b-v1.5 \
	--input-dataset reneuir-2024/re-rank-spot-check-20240624-training
```

### google/flan-t5-xxl

```
docker build -t llm-rankers-flan-t5-xxl --build-arg MODEL_NAME=google/flan-t5-xxl .
```

Test locally + upload to TIRA:
```
tira-run \
	--image llm-rankers-flan-t5-xxl \
	--mount-hf-model google/flan-t5-xxl \
	--input-dataset reneuir-2024/re-rank-spot-check-20240624-training
```

### google/flan-t5-xl

```
docker build -t llm-rankers-flan-t5-xl --build-arg MODEL_NAME=google/flan-t5-xl .
```

Test locally + upload to TIRA:
```
tira-run \
	--image llm-rankers-flan-t5-xl \
	--mount-hf-model google/flan-t5-xl \
	--input-dataset reneuir-2024/re-rank-spot-check-20240624-training
```

### google/flan-t5-large

```
docker build -t llm-rankers-flan-t5-large --build-arg MODEL_NAME=google/flan-t5-large .
```

Test locally + upload to TIRA:
```
tira-run \
	--image llm-rankers-flan-t5-large \
	--mount-hf-model google/flan-t5-large \
	--input-dataset reneuir-2024/re-rank-spot-check-20240624-training
```

### google/flan-t5-small

```
docker build -t llm-rankers-flan-t5-small --build-arg MODEL_NAME=google/flan-t5-small .
```

Test locally + upload to TIRA:
```
tira-run \
	--image llm-rankers-flan-t5-small \
	--mount-hf-model google/flan-t5-small \
	--input-dataset reneuir-2024/re-rank-spot-check-20240624-training
```

