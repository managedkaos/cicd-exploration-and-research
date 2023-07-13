IMAGE_TAG = $(shell git rev-parse --short HEAD)

build:
	docker build -t jenkins_lts:$(IMAGE_TAG) .

clean:
	rm -rf ./jenkins_home
	mkdir ./jenkins_home

up:
	IMAGE_TAG=$(IMAGE_TAG) docker compose up

