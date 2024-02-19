# HowTo: Software Submissions to the SIGIR'24 ReNeuIR Shared Task

You can submit either via code submissions (the preferred [variant 1](variant-1) where you have your code in a prepared git repository that comes with suitable Github actions) or via a prepared Docker image of your approach ([variant 2](variant-2)).
To get you started, please look at our [baseline submissions](../baselines) that you can use as inspiration.
If you have any problems or questions, please do not hesitate to contact us, we are happy to help.

## Step-by-Step Guide

Step 1: Open the task’s [submission page](https://www.tira.io/task-overview/workshop-on-open-web-search/)

Step 2: Click on "SUBMIT", registering your team if necessary.

![Screenshot_20231028_123222](https://github.com/OpenWebSearch/wows-code/assets/10050886/44aece55-c14d-4b02-ba40-0ab095717b52)

## Variant 1: Code Submissions

Step 3: Click on "CODE SUBMISSION" and enter your Github account

![Screenshot_20240109_103935](https://github.com/mam10eks/reneuir-code/assets/10050886/f051391f-8f63-4985-a24d-7cd8de331fb6)

Step 4: Click on "ADD CODE REPOSITORY" which will create a prepared git repository with the baselines and prepared Github actions that dockerize, test, and upload your submission to TIRA.

Step 5: Run the Github Action that dockerizes your approach and uploads it to TIRA. In your Github repository, click on "Actions" => "Upload Docker Software to TIRA" => "Run workflow". Specify the directory containing your approach (e.g., `re-ranking-baseline` for the re-ranking baseline) and the to-be-executed command where `$inputDataset` points to the input and `$outputDir` is the directory where the output file(s) should be stored. The Github action automatically executes the command in the Docker image to check that it works on a small example dataset.

![Screenshot_20240109_105239](https://github.com/mam10eks/reneuir-code/assets/10050886/13e2cc78-df00-4696-8421-218c9ebbe0f2)

## Variant 2: Docker Submissions

Step 3: (On your submission page after step 1 and 2): Click on "DOCKER SUBMISSION" and "CREATE NEW SOFTWARE".

![Screenshot_20231028_123359](https://github.com/OpenWebSearch/wows-code/assets/10050886/11ad7f7e-7e55-4384-b2c3-2740205fc9c4)

Step 4: Follow the instructions, installing `tira` and executing the Docker submission with `tira-run` to test that everything works as expected.
The `tira-run` command will download the data automatically. Adjust `YOUR-COMMAND` where `$inputDataset` points to the input and `$outputDir` is the directory where the output file(s) should be stored. The `tira-run` command automatically checks that the output of the software is valid.

Step 5: Click on PUSH NEW DOCKER IMAGE to get your personalized instructions to push the image to TIRA. Click REFRESH IMAGES after it was pushed to be then able to select if from the Docker Image dropdown. Put the same command you used in 4. into the command text field. Click NEXT and copy the two commands to check your approach another time.
