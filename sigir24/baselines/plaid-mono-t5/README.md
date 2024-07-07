
docker build -t plaid-mono-t5 .

tira-run \
	--input-dataset reneuir-2024/dl-top-10-docs-20240701-training \
	--image plaid-mono-t5 \
	--push true \
	--tira-vm-id reneuir-baselines
