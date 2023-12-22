# HowTo: Software Submissions to the 1st International Workshop on Open Web Search

To start your submission, you should have prepared a Docker image of your approach.
To get you started, please look at our [baseline submissions](../baselines) that you can use as inspiration.
If you have no experience with Docker, please do not hesitate to contact us, we are happy to help you to dockerize your software.

## Step-by-Step Guide

Step 1: Open the task’s [submission page](https://www.tira.io/task-overview/workshop-on-open-web-search/)

Step 2: Click on "SUBMIT", registering your team if necessary.

![Screenshot_20231028_123222](https://github.com/OpenWebSearch/wows-code/assets/10050886/44aece55-c14d-4b02-ba40-0ab095717b52)

Step 3: Click on "DOCKER SUBMISSION" and "CREATE NEW SOFTWARE".

![Screenshot_20231028_123359](https://github.com/OpenWebSearch/wows-code/assets/10050886/11ad7f7e-7e55-4384-b2c3-2740205fc9c4)

Step 4: Follow the instructions, installing `tira` and executing the Docker submission with `tira-run` to test that everything works as expected.
The `tira-run` command will download the data automatically. Adjust `YOUR-COMMAND` where `$inputDataset` points to the input and `$outputDir` is the directory where the output file(s) should be stored. The `tira-run` command automatically checks that the output of the software is valid.

Step 5: Click on PUSH NEW DOCKER IMAGE to get your personalized instructions to push the image to TIRA. Click REFRESH IMAGES after it was pushed to be then able to select if from the Docker Image dropdown. Put the same command you used in 4. into the command text field. Click NEXT and copy the two commands to check your approach another time.
