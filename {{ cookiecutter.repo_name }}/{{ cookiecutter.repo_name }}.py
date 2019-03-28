#!/usr/bin/env python

import argparse
import sys
import os
import time
import random
import datetime
import glob
import functools
import docker

class ProjectCLI(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Command line for {{ cookiecutter.project_name }}',
            usage='''{{ cookiecutter.project_name }}.py <command> [<args>]

{{ cookiecutter.project_name }}.py contains the following commands:
   data       General data related tasks
   model      Train and predict models
   notebook   Deploy notebooks
   build      Create environments to work within
''')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def data(self):
        parser = argparse.ArgumentParser(
            description='General data related tasks')
        parser.add_argument('--source', action='store_true')
        parser.add_argument('--engineer', action='store_true')
        args = parser.parse_args(sys.argv[2:])

    def model(self):
        parser = argparse.ArgumentParser(
            description='Train and predict models')
        parser.add_argument('--train')
        parser.add_argument('--predict')
        args = parser.parse_args(sys.argv[2:])

    def notebook(self):
        parser = argparse.ArgumentParser(
            description='Deploy notebooks')
        args = parser.parse_args(sys.argv[2:])

    def build(self):
        client = docker.from_env()
        parser = argparse.ArgumentParser(
            description='Create environments to work within')
        parser.add_argument('--env', choices=['develop', 'train', 'predict'], default='develop')
        parser.add_argument('--gpu', action='store_true')
        args = parser.parse_args(sys.argv[2:])
	
        if args.env == 'develop':
            proj_dev = '{{ cookiecutter.project_name }}-develop' # attach username...
            # Just volume map the cwd assuming data is present at this point (dvc fetch -r data -> python3 aa.py build)
            client.images.build(path='.', dockerfile='Dockerfile.develop', tag=proj_dev)
            run = functools.partial(client.containers.run, 
                                    proj_dev, 
                                    name=proj_dev,
                                    command="start-notebook.sh --NotebookApp.token=''",
                                    ports={'8888/tcp' : 8888},
                                    working_dir='/home/jovyan/work',
                                    detach=True) # volume={'rops': {'bind': '/home/jovyan/work', 'mode': 'rw'}}
                                # environment={'DATA_PATH': '/home/jovyan/work/data', ....}
            if args.gpu:
                run(runtime='nvidia')
            else:
                run()

if __name__ == '__main__':
    ProjectCLI()
