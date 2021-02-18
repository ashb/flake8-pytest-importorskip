.PHONY: init build test lint pretty precommit_install bump_major bump_minor bump_patch

BIN = .venv/bin/
CODE = flake8_pytest_importorskip

init:
	python3 -m venv .venv
	.venv/bin/pip install -U pip setuptools
	poetry install

build:
	poetry build

test:
	poetry run pytest --verbosity=2 --strict --log-level=DEBUG --cov=$(CODE) --cov-config setup.cfg $(args)

lint:
	poetry run flake8 --statistics --show-source $(CODE) tests
	poetry run pylint --rcfile=setup.cfg $(CODE)
	poetry run mypy $(CODE) tests
	poetry run black --skip-string-normalization --diff --check $(CODE) tests
	poetry run pytest --dead-fixtures --dup-fixtures

pretty:
	poetry run isort --apply --recursive $(CODE) tests
	poetry run black --skip-string-normalization $(CODE) tests

precommit_install:
	echo -e '#!/bin/sh\nmake lint test\n' > .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

bump_major:
	poetry run bumpversion major

bump_minor:
	poetry run bumpversion minor

bump_patch:
	poetry run bumpversion patch
