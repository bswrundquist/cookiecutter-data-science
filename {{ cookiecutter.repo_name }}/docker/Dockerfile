FROM bswrundquist/jn-ext

RUN pip install poetry

WORKDIR /home/jovyan/work
COPY . /home/jovyan/work

RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-interaction
