You can just start a devcontainer in this directory. In this case, your IDE (e.g., Visual Studio Code) handles the docker part (assuming you have docker installed).

If you want to develop without dev containers, you can, (1) build the Docker image (e.g., `docker build -t llm-rankers .`) and start a jupyter server (e.g., `docker run --rm -ti -v ${PWD}:/workspace --entrypoint jupyter -p 8888:8888 llm-rankers notebook --ip 0.0.0.0 --allow-root`).


# Submitted Variants

### google/flan-t5-xl

Build:

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

