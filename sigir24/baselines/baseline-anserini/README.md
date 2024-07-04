
## Indexing

```
tira-run --image anserini \
    --input-dataset reneuir-2024/tiny-sample-20231030-training \
    --command 'java -cp /classes/:/jars/anserini-0.36.1-fatjar.jar io.anserini.index.IndexCollection -collection TirexJsonCollection -index $outputDir/index -input $inputDataset'
```

## Retrieval with BM25

```
tira-run --image anserini \
    --input-dataset reneuir-2024/tiny-sample-20231030-training \
    --command '/retrieval.sh $inputDataset -bm25 -output $outputDir/run.txt'
```

## Retrieval with QLD

```
tira-run --image anserini \
    --input-dataset reneuir-2024/tiny-sample-20231030-training \
    --command '/retrieval.sh $inputDataset -qld -output $outputDir/run.txt'
```

## Retrieval with inl2

```
tira-run --image anserini \
    --input-dataset reneuir-2024/tiny-sample-20231030-training \
    --command '/retrieval.sh $inputDataset -inl2 -output $outputDir/run.txt'
```

## Retrieval with SPL

```
tira-run --image anserini \
    --input-dataset reneuir-2024/tiny-sample-20231030-training \
    --command '/retrieval.sh $inputDataset -spl -output $outputDir/run.txt'
```

## Retrieval with f2log

```
tira-run --image anserini \
    --input-dataset reneuir-2024/tiny-sample-20231030-training \
    --command '/retrieval.sh $inputDataset -f2log -output $outputDir/run.txt'
```

## Retrieval with f2exp

```
tira-run --image anserini \
    --input-dataset reneuir-2024/tiny-sample-20231030-training \
    --command '/retrieval.sh $inputDataset -f2exp -output $outputDir/run.txt'
```
