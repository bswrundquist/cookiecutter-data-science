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
   train      Train models
   predict    Use trained models for prediction
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

    def train(self):
        parser = argparse.ArgumentParser(
            description='Train models')
        parser.add_argument('--verb', choices=['example'])
        parser.add_argument('--name')
        parser.add_argument('--parameters')
        parser.add_argument('--predict')
        args = parser.parse_args(sys.argv[2:])

    def predict(self):
        parser = argparse.ArgumentParser(
            description='Use trained models for prediction')
        parser.add_argument('--verb')
        parser.add_argument('--name')
        parser.add_argument('--parameters')
        parser.add_argument('--checkpoint')
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
        parser.add_argument('--port', type=int, default=8888)
        parser.add_argument('--gpu', action='store_true')
        args = parser.parse_args(sys.argv[2:])
        
        proj_env = '{{ cookiecutter.project_name }}-{env}'.format(env=args.env)
        dockerfile = 'Dockerfile.{env}'.format(env=args.env)

        image_params = {
            'path': '.',
            'dockerfile': dockerfile,
            'tag': proj_env
        }
        client.images.build(**image_params)

        run_params = {
            'name': image_params['tag'],
            'image': image_params['tag'],
            'environment': {'ENV': args.env},
            'user': 'root',
            'detach': True
        }

        if args.gpu:
            run_params['runtime'] = 'nvidia'
            run_params['name'] = '{name}-gpu'.format(name=run_params['name'])

        base_run = functools.partial(client.container.run, **run_params)
        cwd = os.getcwd()

        if args.env == 'develop':
            env_params = {
                'command': "start-notebook.sh --NotebookApp.token=''",
                'ports': {'8888/tcp' : args.port},
                'volumes': {cwd: {'bind': '/home/jovyan/work', 'mode': 'rw'}},
                'working_dir': '/home/jovyan/work'
            }

        elif args.env == 'train':
            env_params = create_train_or_predict_params(which='train', args=args)

        elif args.env == 'predict':
            env_params = create_train_or_predict_params(which='predict', args=args)

        base_run(**env_params)

def create_train_or_predict_params(which, args):
    if not args.command:
        args.command = 'python /opt/{{ cookiecutter.project_name }}.py {which}'.format(which=which)
    if args.name:
        args.command += ' --name={name}'.format(name=args.name)

    cwd = os.getcwd()
    params = {
        'command': args.command,
        'volumes': {cwd: {'bind': '/opt', 'mode': 'rw'}},
        'working_dir': '/opt'
    }

    return params

if __name__ == '__main__':
    ProjectCLI()
