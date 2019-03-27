#!/usr/bin/env python

import argparse
import sys
import os
import time
import random
import datetime
import glob
import functools


class {{ cookiecutter.project_name }}CLI(object):

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
        parser.add_argument('--env', choices=['develop', 'train', 'predict'], default='develop')
        args = parser.parse_args(sys.argv[2:])

    def model(self):
        parser = argparse.ArgumentParser(
            description='Train and predict models')
        parser.add_argument('--train')
        parser.add_argument('--predict')
        args = parser.parse_args(sys.argv[2:]

    def notebook(self):
        parser = argparse.ArgumentParser(
            description='Deploy notebooks')
        args = parser.parser_args(sys.argv[2:])

    def build(self):
        parser = argparse.ArgumentParser(
            description='Create environments to work within')
        parser.add_argument('--develop', action='store_true')
        parser.add_argument('--train', action='store_true')
        parser.add_argument('--predict', action='store_true')
        args = parser.parser_args(sys.argv[2:])
	
        if args.develop:
            develop_tag = '{{ cookiecutter.project_name }}-develop' # attach username....
            client.build(path='.', dockerfile='Dockerfile.develop', tag=develop_tag)
            client.containers.run(develop_tag, 
                                name=develop_tag,
                                command="start-notebook.sh --NotebookApp.token=''",
                                ports={'8888/tcp' : 8888},
                                runtime='nvidia',
                                working_dir='/home/jovyan/work',
                                detach=True) # volume={'rops': {'bind': '/home/jovyan/work', 'mode': 'rw'}}
                                # environment={'DATA_PATH': '/home/jovyan/work/data', ....}


if __name__ == '__main__':
    {{ cookiecutter.project_name }}CLI()
