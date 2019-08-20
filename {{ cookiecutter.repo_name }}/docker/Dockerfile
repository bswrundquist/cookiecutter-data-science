FROM bswrundquist/jn-ext

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | /opt/conda/bin/python

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=0.12.16

# System deps:
RUN /opt/conda/bin/pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /home/jovyan/work
COPY poetry.lock pyproject.toml /home/jovyan/work/

# Project initialization:
RUN poetry config settings.virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /home/jovyan/work