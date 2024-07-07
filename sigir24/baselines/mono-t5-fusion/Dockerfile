# docker build -t fusion-t5 .
FROM webis/ir-lab-wise-2023:0.0.4

# Update the tira command to use the latest version
RUN pip3 uninstall -y tira \
	&& pip3 install tira

ADD . /app

ENTRYPOINT [ "/run-notebook.py", "--input", "$inputDataset", "--notebook", "/app/fusion.ipynb", "--output", "$outputDir" ]

