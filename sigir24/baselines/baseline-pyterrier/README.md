# Baseline Submission for a Re-Ranker in the ReNeuIR Shared task

This is a baseline re-ranker that increases the score of each document by 1.

You can run it directly via (please install `tira` via `pip3 install tira`, Docker, and Python >= 3.7 on your machine): 

```
tira-run \
	--input-dataset workshop-on-open-web-search/re-ranking-20231027-training \
	--image mam10eks/reneuir-baselines:re-ranker-0.0.1
```

## Development

You can build the Docker image via:

```
docker build -t mam10eks/reneuir-baselines:re-ranker-0.0.1 .
```

To publish the image to dockerhub, run:

```
docker push mam10eks/reneuir-baselines:re-ranker-0.0.1
```
