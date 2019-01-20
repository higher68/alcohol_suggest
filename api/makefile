IMAGE_NAME=alcohol_suggest_api
CONATAINER_NAME=${IMAGE_NAME}

ALCOHOL_SUGGEST_API_IP=$(shell docker inspect -f "{{.NetworkSettings.IPAddress}}" alcohol_suggest_api)

build:
	docker build \
		-t ${IMAGE_NAME} .

run:
	docker-compose \
		up \
		-d

rm:
	docker rm \
		-f ${CONATAINER_NAME}

exec:
	docker exec \
		-it ${CONATAINER_NAME} \
		bash

restart:
	docker-compose \
		restart

