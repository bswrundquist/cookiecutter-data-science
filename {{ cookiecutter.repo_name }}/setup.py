from setuptools import setup
from setuptools import find_packages

from glob import glob
from os.path import splitext
from os.path import basename

setup(
    name='{{ cookiecutter.project_name }}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.team_name }}'
)
