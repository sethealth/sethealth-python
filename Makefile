
venv:
	pipenv sync --dev --pre --bare

build: venv
	pipenv run pipenv-setup sync
	pipenv run python setup.py sdist bdist_wheel

release: clean fmt-check dependencies-check lint test build
	pipenv run twine upload dist/*

test: venv
	pipenv run python -m tox -p auto
	pipenv run python -m tox -e noenvs

fmt: venv
	pipenv run python -m tox -e fmt

fmt-check: venv
	pipenv run python -m tox -e fmt -- --check --verbose

dependencies: venv
	pipenv run pipenv-setup sync --dev

dependencies-check: venv
	pipenv run pipenv-setup check

lint: venv
	pipenv run python -m tox -e lint

clean:
	rm -rf dist/ build/
	pipenv --venv | xargs rm -rf


.PHONY: venv test ci coveralls fmt fmtcheck lint clean