SHELL=./make-venv
export FLASK_APP=app
export FLASK_ENV=development

all: help

.PHONY: help
help: Makefile
	@echo "Choose a command run:"
	@(sed -n "s/^## //p" Makefile | column -t -s ":" | sed -e "s/^/  /")

## install: installs dependencies under venv
.PHONY: install
install:
	python3 -m venv venv
	pip install --upgrade pip
	make post-install

.PHONY: post-install
post-install:
	pip3 install -r requirements.txt
	flask init-db

## run: run development flask server
run:
	flask run

## clean: remove venv directory
.PHONY: clean
clean:
	rm -rf venv

## test: run basic unit tests
.PHONY: test
test:
	python -m pytest tests/
