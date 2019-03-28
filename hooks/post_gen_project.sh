#!/usr/bin/env bash

PROJECT_NAME='{{ cookiecutter.project_name }}'
echo "Initializing project $PROJECT_NAME"

sudo apt -y install python3-pip
sudo pip3 install dvc[gs]
sudo pip3 install cookiecutter

echo "Setting up code versioning"
git init
git config --global credential.https://source.developers.google.com.helper gcloud.sh
git remote add origin https://source.developers.google.com/p/esai-222021/r/$PROJECT_NAME
git push --set-upstream origin master

echo "Setting up data versioning"
dvc init
git commit -m 'initialize DVC'

dvc remote add -d checkpoints gs://$PROJECT_NAME/checkpoints
dvc remote add -d data gs://$PROJECT_NAME/data
git add .dvc/config
git commit -m 'add data and checkpoints to dvc'
git push --set-upstream origin master
