# AWS 2-step CodePipeline for Automated tests

## CodeCommit -> CodeDeploy -> webapp on EC2

## Setup

Download _latest Python 3.x (64 bit)_ executable (msi) installer from [python.org](https://www.python.org/downloads/release)

Verify python/pip are installed:

    python --version
    pip --version

 Create a virtual environment and install python libs (Windows CMD)

    python -m venv venv
    venv\Scripts\activate.bat
	pip install --upgrade pip
	pip install -r reqs.txt
    seleniumbase install chromedriver latest

## Run tests

### Local machine

    pytest