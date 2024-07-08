You can just start a devcontainer in this directory. In this case, your IDE (e.g., Visual Studio Code) handles the docker part (assuming you have docker installed).

If you want to develop without dev containers, you can, (1) build the Docker image (e.g., `docker build -t rankllama .`) and start a jupyter server (e.g., `docker run --rm -ti -v ${PWD}:/workspace --entrypoint jupyter -v ${HF_HOME}:/root/.cache/huggingface:ro -p 8888:8888 rankllama notebook --ip 0.0.0.0 --allow-root`).

```
tira-run \
	--image rankllama \
	--mount-hf-model meta-llama/Llama-2-7b-hf castorini/rankllama-v1-7b-lora-passage \
	--input-dataset reneuir-2024/re-rank-spot-check-20240624-training
```

