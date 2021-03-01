.PHONY: help init build test lint pretty precommit_install bump_major bump_minor bump_patch

BIN = .venv/bin/
CODE = flake8_pytest_importorskip

help: # Make help to show possible targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

init:  ## Create a virtualenv for dev
	python3 -m venv .venv
	.venv/bin/pip install -U pip setuptools
	poetry install

build:  ## Build the sdist/wheel packages
	poetry build

test:  ## Test the project
	poetry run pytest --verbosity=2 --strict --log-level=DEBUG --cov=$(CODE) --cov-config setup.cfg $(args)

lint:  ## Check code for style
	poetry run flake8 --statistics --show-source $(CODE) tests
	poetry run pylint --rcfile=setup.cfg $(CODE)
	poetry run mypy $(CODE) tests
	poetry run black --diff --check $(CODE) tests
	poetry run pytest --dead-fixtures --dup-fixtures

pretty: ## Prettify the code
	poetry run isort --apply --recursive $(CODE) tests
	poetry run black $(CODE) tests

precommit_install: ## Install simple pre-commit checks
	echo -e '#!/bin/sh\nmake lint test\n' > .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

bump_major: ## Release a new major version
	poetry run bumpversion major

bump_minor: ## Release a new minor version
	poetry run bumpversion minor

bump_patch: ## Release a new patch version
	poetry run bumpversion patch
