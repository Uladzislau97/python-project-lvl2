install:
	@poetry install

build: clear
	@poetry build

publish: build
	@poetry publish --repository testpypi

run:
	@poetry run gendiff

clear:
	if [ -d "dist" ]; then rm -r dist; fi

lint:
	@poetry run flake8 gendiff

test:
	pytest

coverage:
	pytest --cov=gendiff/ tests/

coverage-xml:
	pytest --cov=gendiff/ tests/ --cov-report xml