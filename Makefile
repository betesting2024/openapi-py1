install:
	python ./setup.py build 
	python ./setup.py install

build:
	@echo "nothing to build.python!"

test:
	pip install -r ./test-requirements.txt
	cd server/openapi_server/test && pytest -vv

generate:
	@echo "warning: this will overwrite your changes!"
	mkdir -p server && cd server && \
		openapi-generator-cli.cmd generate -g python-flask -i ..\bloom-api.yaml
	mkdir -p client && cd client && \
		openapi-generator-cli.cmd generate -g python -i ..\bloom-api.yaml

depends:
	pip install -r ./requirements.txt
	
