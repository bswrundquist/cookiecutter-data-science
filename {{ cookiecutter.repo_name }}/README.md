{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Setup Workspace
----------------

Using Docker and Makefile we can spin up a workspace using Jupyter notebook according the Dockerfile in the docker folder.

```bash
make workspace
```
Or to use a specific port run the following.

```bash
make workspace WORKSPACE_PORT=9999
```

Project Organization
------------

├── Makefile
├── README.md
├── api.py
├── data
│   ├── external
│   ├── raw
│   └── transform
├── docker
│   └── Dockerfile
├── docs
├── models
├── poetry.lock
├── pyproject.toml
├── references
├── reports
│   └── figures
├── test_environment.py
├── tox.ini
├── {{cookiecutter.repo_name}}
│   ├── data
│   ├── models
│   └── plots
└── workspaces
    ├── WORKSPACE-TEMPLATE.Rmd
    └── WORKSPACE-TEMPLATE.ipynb

------------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
