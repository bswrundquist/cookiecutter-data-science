#!/usr/bin/env bash

PROJECT_NAME='{{ cookiecutter.project_name }}'

#apt -y install python3-pip
pip3 install dvc[gs]

# set env variable ENV = develop, train
dvc init
git commit -m 'initialize DVC'

dvc remote add -d data gs://$PROJECT_NAME/data
dvc remote add -d checkpoints gs://$PROJECT_NAME/checkpoints
git commit -m 'add data and checkpoints to dvc'
git push


