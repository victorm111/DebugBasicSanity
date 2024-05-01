.DEFAULT_GOAL := help
.PHONY: coverage deps help lint push test

init:
	pip install -r requiremenmts.txt

coverage:  ## Run tests with coverage
	coverage erase
	coverage run --include=podsearch/* -m pytest -ra
	coverage report -m
	coverage html

deps:  ## Install dependencies
	pip install black coverage flake8 mccabe mypy pylint pytest tox

lint:  ## Lint and static-check
	flake8 src/debug_basic_sanity
	pylint src/debug_basic_sanity
	mypy src/debug_basic_sanity

push:  ## Push code with tags
	git push && git push --tags

test:  ## Run tests
	pytest -ra tests