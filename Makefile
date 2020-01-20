install:
	@poetry install

build: clear
	@poetry build

publish: build
	twine upload --repository testpypi dist/* --config-file .pypirc

run:
	@poetry run gendiff

clear:
	if [ -d "dist" ]; then rm -r dist; fi

lint:
	@poetry run flake8 gendiff

test:
	pytest

test-coverage:
	pytest --cov=gendiff/ tests/