# flake8-pytest-importorskip

[![pypi](https://badge.fury.io/py/flake8-pytest-importorskip.svg)](https://pypi.org/project/flake8-pytest-importorskip)
[![Python: 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://pypi.org/project/flake8-pytest-importorskip)
[![Downloads](https://img.shields.io/pypi/dm/flake8-pytest-importorskip.svg)](https://pypistats.org/packages/flake8-pytest-importorskip)
[![Build Status](https://travis-ci.org/ashb/flake8-pytest-importorskip.svg?branch=master)](https://travis-ci.org/ashb/flake8-pytest-importorskip)
[![Code coverage](https://codecov.io/gh/ashb/flake8-pytest-importorskip/branch/master/graph/badge.svg)](https://codecov.io/gh/ashb/flake8-pytest-importorskip)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://en.wikipedia.org/wiki/Apache_License)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Description

Treat `pytest.importorskip` as an import statement, not code, to silence the "module level import not at top of file" (E402) from pycodestyle

It allows code such as this to pass without having to globally disable E402.

It does this in a _slightly_ hacky way, so it may break in future versions of flake8 or pycodestyle.


### Checks:

None

## Installation

    pip install flake8-pytest-importorskip

## Usage

`flake8 <your code>`

## For developers

### Create venv and install deps

    make init

### Install git precommit hook

    make precommit_install

### Run linters, autoformat, tests etc.

    make pretty lint test

### Bump new version

    make bump_major
    make bump_minor
    make bump_patch

## License

Apache 2.0

## Change Log

Unreleased
-----

* ...

1.0.0 - 2021-02-19
-----

* initial
