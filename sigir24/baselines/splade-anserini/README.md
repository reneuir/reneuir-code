## Retrieval with Anserini

docker build -t anserini-splade-search -f Dockerfile.anserini .

```
tira-run \
    --image anserini-splade-search \
    --input-dataset reneuir-2024/dl-top-10-docs-20240701-training \
    --command '/retrieval.sh $inputDataset -output $outputDir/run.txt'
```

## Building an Anserini Index

docker build -t anserini-splade-search -f Dockerfile.anserini .

```
tira-run \
	--image anserini-splade-search \
	--input-dataset reneuir-2024/tiny-sample-20231030-training
```

## Encoding of the Documents and Queries
docker build -t mam10eks/anserini-splade .

docker run --rm -ti -v ${PWD}:/app -w /app --entrypoint bash anserini-splade

```
tira-run \
	--image mam10eks/anserini-splade \
	--input-dataset reneuir-2024/tiny-sample-20231030-training
```


