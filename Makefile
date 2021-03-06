  
VENV_NAME?=venv

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: setup.py
	pip install --upgrade pip virtualenv setuptools wheel twine
	@test -d $(VENV_NAME) || python -m virtualenv --clear $(VENV_NAME)
	${VENV_NAME}/bin/python -m pip install -U pip tox
	${VENV_NAME}/bin/python -m pip install -e .
	@touch $(VENV_NAME)/bin/activate

build: venv
	python setup.py sdist bdist_wheel

release: clean fmtcheck lint test build 
	twine upload dist/*

test: venv
	@${VENV_NAME}/bin/tox -p auto $(TOX_ARGS)
	@${VENV_NAME}/bin/tox -e noenvs

fmt: venv
	@${VENV_NAME}/bin/tox -e fmt

fmtcheck: venv
	@${VENV_NAME}/bin/tox -e fmt -- --check --verbose

lint: venv
	@${VENV_NAME}/bin/tox -e lint

clean:
	@rm -rf $(VENV_NAME) dist/

.PHONY: venv test ci coveralls fmt fmtcheck lint clean