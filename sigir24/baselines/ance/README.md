
```
docker build -t ance-retrieval .
```


```
tira-run \
    --input-dataset reneuir-2024/dl-top-10-docs-20240701-training \
    --image ance-retrieval \
    --push true \
    --tira-vm-id ows
```
