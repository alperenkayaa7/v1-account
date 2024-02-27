# v1-account

## Description

This is a microservice that provides the ability to manage trade journals. It is a RESTful API that allows users to create, read, and update trade journals. 

## Installation

To install the project, you will need to have the following installed:

- [Python 3.8](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop)
- [AWS CLI](https://aws.amazon.com/cli/)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

## Usage

To run the project, you will need to run the following commands:

### Install Dependencies

```bash
pip3 install -r source/requirements.txt --target ./source/package/
```

### Run the project locally

```bash
sam local start-api --parameter-overrides 'ParameterKey=UserPoolArn,ParameterValue=arn:aws:cognito-idp:eu-central-1:847495510557:userpool/eu-central-1_BWXrJCpu0'
```

### Deploy the project

```bash
sam deploy --guided
```



