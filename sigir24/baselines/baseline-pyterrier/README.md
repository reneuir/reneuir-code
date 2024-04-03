# ReNeuIR 2024 Pyterrier Baseline

This is a PyTerrier/ir_datasets baseline for ReNeuIr covering (1) indexing, (2) retrieval, and (3) re-ranking.


## Preparation

Please install `docker`, Python >= 3.7, and `tira-run` on your machine (`pip3 uninstall -y tira && pip3 install tira`).

Build the docker image via:

```
docker build -t reneuir-baseline-pyterrier .
```


## Step 1: Indexing

There is already a PyTerrier indexing component in TIRA that indexes documents with the `default_text()` field using the standard stopwords and Porter stemmer. If you want to create a custom index, you can modify the [indexing.py](indexing.py) script, otherwise, you can just re-use the existing index (which we assume for the following).


## Step 2: Retrieval

The [retrieval.py](retrieval.py) script retrieves with BM25 with default configuration, run it via:

```
tira-run \
    --image reneuir-baseline-pyterrier \
    --input-dataset reneuir-2024/tiny-sample-20231030-training \
    --command '/retrieval.py'
```

The resulting run file is in `tira-output/run.txt`.

## Step 3: Re-Ranking

The [re-ranking.py](re-ranking.py) script implements a dummy re-ranker that just increases the score of the previous stage  by 1, run it via:

```
tira-run \
	--input-dataset workshop-on-open-web-search/re-ranking-20231027-training \
	--image reneuir-baseline-pyterrier \
	--command '/re-ranking.py'
```

The resulting run file is in `tira-output/run.txt`.
