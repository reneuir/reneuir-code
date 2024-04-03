# A prepared image with python3.10, java 11, ir_datasets, tira, and PyTerrier installed 
FROM webis/ir-lab-wise-2023:0.0.4

# Update the tira command to use the latest version
RUN pip3 uninstall -y tira \
	&& pip3 install tira
	
# Install additional dependencies here, e.g., Maven as example if you like to use java
RUN echo "you can install additional dependencies here" \
	&& apt-get install -y maven

#Add files to the image if they are needed for the submission
#ADD your-file /location-in-docker-image/


