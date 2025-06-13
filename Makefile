CONTAINER_NAME := $(shell docker compose ps -q | head -n 1)

test:
	docker exec -it $(CONTAINER_NAME) \
	pytest -v \
	--cov=marketbridge.services \
	--cov-report=term-missing

build:
	docker compose up --build -d