# Submitted Variants

### webis/monoelectra-base

```
docker build -t monoelectra-base --build-arg MODEL_NAME=monoelectra-base .
```

Test locally + upload to TIRA:
```
tira-run \
	--image monoelectra-base \
	--mount-hf-model webis/monoelectra-base \
	--input-dataset reneuir-2024/re-rank-spot-check-20240624-training
```

### webis/monoelectra-large

```
docker build -t monoelectra-large --build-arg MODEL_NAME=monoelectra-large .
```

Test locally + upload to TIRA:
```
tira-run \
	--image monoelectra-large \
	--mount-hf-model webis/monoelectra-large \
	--input-dataset reneuir-2024/re-rank-spot-check-20240624-training
```