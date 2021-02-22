.PHONY : create-env
create-env:
	conda env create

.PHONY : export-env
export-env:
	conda env export --from-history > environment.yml

.PHONY : install
install:
	poetry install

.PHONY: test
test :
	coverage run

.PHONY : format
format :
	isort .
	black .

.PHONY : lint
lint:
	flake8 .
	mypy .

.PHONY : apidoc
apidoc:
	sphinx-apidoc -o docs/source/ {{cookiecutter.module_name}}
