PROFILE=pluralsight
FUNCTION=
CODE=$(shell ls *.py)

hello:
	@echo "Here are the targets for this Makefile:"
	@echo "  lint   - run pylint on the code"
	@echo "  black  - run black on the code"
	@echo "  test   - run the tests"
	@echo "  build  - build the lambda.zip file"
	@echo "  deploy - deploy the lambda.zip file to AWS"
	@echo "  clean  - remove the lambda.zip file"
	@echo "  all    - clean, test, build, and deploy"
	@echo
	@echo
	@echo "You must set the PROFILE and FUNCTION variables to use the"
	@echo "deploy target.  For example:"
	@echo
	@echo "  make PROFILE=foo FUNCTION=bar deploy"
	@echo
	@echo "  PROFILE  - the AWS profile to use for the deployment."
	@echo "  FUNCTION - the name of the existing lambda function to update."

requirements:
	pip install --requirement requirements-development.txt

lint:
	pylint --disable=R,C $(CODE)

black:
	black --check $(CODE)

test:
	ENVIRONMENT=testing python -m unittest -v index_test

build:
	zip lambda.zip index.py data.json

deploy:
	aws --profile=$(PROFILE) lambda update-function-code \
		--function-name=$(FUNCTION) \
		--zip-file fileb://lambda.zip

clean:
	rm -f lambda.zip

all: clean test build deploy

.PHONY: test build deploy all clean

