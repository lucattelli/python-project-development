ci:
	poetry run black --check --diff python_project_development tests
	poetry run isort --check-only --diff python_project_development tests
	poetry run pylint python_project_development tests
	poetry run mypy python_project_development tests


clean:
	rm -rf dist

deep-clean:
	make clean
	rm -rf .venv

fmt:
	poetry run black python_project_development tests
	poetry run isort python_project_development tests

install:
	poetry lock --no-update
	poetry install

lint:
	poetry run pylint python_project_development tests

run:
	poetry run python python_project_development/main.py

type:
	poetry run mypy python_project_development tests

test:
	ENVIRONMENT=test poetry run pytest tests

.PHONY: test
