IMAGE_NAME=alcohol_suggest_db
CONTAINER_NAME=${IMAGE_NAME}

ALCOHOL_SUGGEST_DB_IP=$(shell docker inspect -f "{{.NetworkSettings.IPAddress}}" alcohol_suggest_db)

build:
	docker build \
		-t ${IMAGE_NAME} .

run:
	docker-compose \
		up \
		-d

rm:
	docker rm \
		-f ${CONTAINER_NAME}

exec:
	docker exec \
		-it ${CONTAINER_NAME} \
		bash

restart:
	docker-compose \
		restart
