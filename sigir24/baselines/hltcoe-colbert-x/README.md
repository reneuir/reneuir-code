# PLAID-X at ReNeuIR

This directory has the code (dockerized the [PLAID-X for CLIR notebook]() for execution in TIRA) for PLAID-X on English at ReNeuIR.

You can just start a devcontainer in this directory. In this case, your IDE (e.g., Visual Studio Code) handles the docker part (assuming you have docker installed).

If you want to develop without dev containers, you can, (1) build the Docker image (e.g., `docker build -t plaid-x .`) and start a jupyter server (e.g., `docker run --rm -ti -v ${PWD}:/workspace --entrypoint jupyter -p 8888:8888 plaid-x notebook --ip 0.0.0.0 --allow-root`).

