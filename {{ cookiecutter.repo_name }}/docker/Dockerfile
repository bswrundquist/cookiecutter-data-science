FROM bswrundquist/jn-ext

RUN pip install poetry

RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-interaction

WORKDIR /home/jovyan/work
COPY . /home/jovyan/work