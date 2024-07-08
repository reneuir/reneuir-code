# Submitted Variants

### webis/set-encoder-base

```
docker build -t set-encoder-base --build-arg MODEL_NAME=webis/set-encoder-base .
```

Test locally + upload to TIRA:
```
tira-run \
	--image set-encoder-base \
	--mount-hf-model webis/set-encoder-base \
	--input-dataset reneuir-2024/re-rank-spot-check-20240624-training
```

### webis/set-encoder-large

```
docker build -t set-encoder-large --build-arg MODEL_NAME=webis/set-encoder-large .
```

Test locally + upload to TIRA:
```
tira-run \
	--image set-encoder-large \
	--mount-hf-model webis/set-encoder-large \
	--input-dataset reneuir-2024/re-rank-spot-check-20240624-training
```