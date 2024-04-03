# ReNeuIR 2024 Baseline Without Dependencies

As ReNeuIR aims to compare the efficiency of systems, we provide a baseline that works without any dependencies. Below, we show a three step pipeline for ReNeuIR: (1) indexing, (2) retrieval, and (3) re-ranking. Everything is mocked to only highlight how things could be used without frameworks. If you prefer some more easy to read code (e.g., with ir_datasets), we also have more advanced baselines with [Anserini/PySerini](../baseline-anserini) and [PyTerrier](../baseline-pyterrier) available, still, this baseline shows how you could do everything with full control.

## Preparation

Please install `docker` and `tira-run` on your machine (`pip3 uninstall -y tira && pip3 install tira`).

Now, please have a look into the data format, e.g., via:

```
tira-cli download --dataset tiny-sample-20231030-training
```

This downloads a tiny sample dataset and prints the location to stdout.

Build the docker image via:

```
docker build -t reneuir-baseline-without-dependencies .
```

## Step 0: Input/Output Basics in TIRA

TIRA expects that software reads its inputs from a directory and writes its outputs to a dedicated directory. Therefore, the following environment variables are available:

- `TIRA_INPUT_DATASET`: points to the directory that contains the input dataset (identical format to what you get for `tira-cli download --dataset tiny-sample-20231030-training`).
- `TIRA_OUTPUT_DIR`: points to the directory where the outputs should be stored.
- `TIRA_INPUT_RUN`: If your software uses the outputs of some other software as additional inputs, this points to the directory with the ouptuts of the previous software (e.g., an Index).

## Step 1: Indexing

The [indexing.py](indexing.py) script builds a pseudo index.

Run the following command to create this index in a directory `index`:

```
tira-run \
    --image reneuir-baseline-without-dependencies \
    --input-dataset reneuir-2024/tiny-sample-20231030-training \
    --output-directory index \
    --command '/indexing.py -i $TIRA_INPUT_DATASET -o $TIRA_OUTPUT_DIR'
```

The resulting "pseudo index" is now in the file `index/pseudo_index.jsonl.gz`.

## Step 2: Retrieval

The [retrieval.py](retrieval.py) script creates a pseudo run file that just lists the first 5 document ids per query.

Run it via:

```
tira-run \
    --image reneuir-baseline-without-dependencies \
    --input-dataset reneuir-2024/tiny-sample-20231030-training \
    --input-run-directory index \
    --command '/retrieval.py --input $TIRA_INPUT_DATASET --output $TIRA_OUTPUT_DIR --index $TIRA_INPUT_RUN'
```

The resulting run file is in `tira-output/run.txt`.


## Step 3: Re-Ranking

Now, please have a look into the data format for re-rankers, e.g., via:

```
tira-cli download --dataset re-ranking-20231027-training
```

This downloads a tiny sample re-ranking dataset and prints the location to stdout.

The [re-ranking.py](re-ranking.py) script creates a pseudo run file that just increases the score of the previous stage by 1.

```
tira-run \
    --image reneuir-baseline-without-dependencies \
    --input-dataset workshop-on-open-web-search/re-ranking-20231027-training \
    --command '/re-ranking.py -i $TIRA_INPUT_DATASET -o $TIRA_OUTPUT_DIR'
```

The resulting run file is in `tira-output/run.txt`.
