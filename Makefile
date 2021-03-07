APP_NAME=`cat APP_NAME`

# TODO build sphynx docs
.PHONY: docs
docs:
	@echo "not implememted"

# Install install required libraries
.PHONY: init
init:
	pip3 install -r requirements.txt
	pip3 install -r requirements-dev.txt

# inspect security issues in python code
.PHONY: inspect
inspect:
	bandit -r ./$(APP_NAME)

# run with python
.PHONY: run
run:
	python3 -m $(APP_NAME) $(arg1)
.PHONY: docker-it

# enable ssh agent
.PHONY: ssh
ssh:
	eval $(ssh-agent) && ssh-add

# run python tests with pytest
.PHONY: test
test:
	pytest -rA tests

# run pytest with coverage
.PHONY: test-cov
test-cov:
	pytest -rA --cov=$(APP_NAME) tests/
