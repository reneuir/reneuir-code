docker build -t anserini-splade .

docker run --rm -ti -v ${PWD}:/app -w /app --entrypoint bash anserini-splade

```
tira-run \
	--image anserini-splade \
	--input-dataset reneuir-2024/tiny-sample-20231030-training
```


