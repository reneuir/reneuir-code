
Build the docker image: `docker build -t mono-duo-t5 .`

re-rank the top-25:

```
tira-run \
	--image mono-duo-t5 \
	--input-dataset reneuir-2024/dl-top-1000-docs-20240701-training \
	--command '/reranking.py --input-dataset $inputDataset --output $outputDir --top-k 25'
```
