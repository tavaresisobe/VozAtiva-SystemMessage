SERVICE_PORT = 8000

#include .env
export

run:
	poetry run uvicorn --reload --host 0.0.0.0 --port ${SERVICE_PORT} server:main

lint:
	pylint -j 4 *  --rcfile=.pylintrc --output-format=colorized --ignore=swagger.json,tests,Pipfile,venv --disable=R0801 --fail-under=10 --disable=C
