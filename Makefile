.POSIX:

.PHONY: init
init: ## initializes python venv
	python3 -m venv venv

.PHONY: prov init
prov: ## provisions venv with server dependencies
	. ./venv/bin/activate && \
	pip install -r requirements.txt && \
	deactivate

.PHONY: help
help: ## show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | \
	sort | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
