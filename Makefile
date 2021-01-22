.POSIX:

.PHONY: init
init: ## initializes python venv
	python3 -m venv venv

.PHONY: prov init init_db
prov: ## provisions venv with server dependencies
	. ./venv/bin/activate && \
	pip install -r requirements.txt && \
	deactivate

.PHONY: run
run: ## runs the server for testing
	. ./venv/bin/activate && \
	python src/hello.py && \
	deactivate

.PHONY: init_db
init_db: ## initializes the sqlite db
	mkdir -p ./db && \
	sqlite3 db/temperature.sqlite < db.init

.PHONY: test
test: ## runs the example script for testing
	. ./venv/bin/activate && \
	python src/example.py && \
	deactivate

.PHONY: help
help: ## show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | \
	sort | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
