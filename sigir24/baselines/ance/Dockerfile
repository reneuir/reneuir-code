#docker build -t ance-retrieval .
FROM webis/workshop-on-open-web-search-submissions:ows-mam10eks-w-0-0-1-tira-docker-software-id-sunny-throw

ADD retrieval-with-ance.ipynb /

ENTRYPOINT [ "/run-pyterrier-notebook.py", "--input", "$inputDataset", "--output", "$outputDir", "--notebook", "/retrieval-with-ance.ipynb" ]
