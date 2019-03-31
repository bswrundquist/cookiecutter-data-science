{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── engineer       <- Finalized data with schema, scaler, imputer, etc needed for train and predict.
    │   └── source         <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                      the creator's initials, and a short `-` delimited description, e.g.
    │   │                      `1.0-jqp-initial-data-exploration`.
    │   │
    │   └── local          <- Create with a reasonable dataset compared to working environment.
    │   └── deployed       <- Deploy creation of notebook through a job.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting.
    │
    ├── Dockerfile.develop <- Define environment for development.
    │
    ├── Dockerfile.train   <- Define environment to train model.
    │
    ├── Dockerfile.predict <- Define environment to deploy model.
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported.
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module.
    │   │
    │   ├── data           <- Code to download or generate data.
    │   │   └── source.py
    │   │   └── engineer.py
    │   │   └── plot.py
    │   │
    │   └── verbs          <- Different models needed to create final output.
    │       │                 predictions.
    │       └── example    <- Example of folder and files for modeling effort.
    │           └── train.py
    │           └── predict.py
    │           └── plot.py
    │           └── parameters.json
    │   
    │   
    ├── tox.ini            <- tox file with settings for running tox; see tox.testrun.org.
    │
    └── {{ cookiecutter.repo_name }}.py              <- CLI to tie everything together.

--------

{{cookiecutter.stakeholders}}

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
