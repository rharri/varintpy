#!/usr/bin/env bash

isort src/ --profile black
flake8 src/
mypy src/