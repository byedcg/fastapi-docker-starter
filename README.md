# fastapi-docker-starter

FastAPI boilerplate for easy development and deployment.

## Development

### Run the server

```shell
uvicorn app.main:app --reload
```

### Endpoints

```shell
localhost:8000/
localhost:8000/docs
localhost:8000/redoc
```

## Setup Poetry

```bash
poetry init
poetry config --list
poetry config virtualenvs.in-project true
poetry install
poetry export -f requirements.txt -o requirements-freeze.txt --without-hashes
```

### Activate

```bash
poetry shell
```

### Run scripts

```bash
poetry run format
poetry run lint
poetry run start
poetry run test
```