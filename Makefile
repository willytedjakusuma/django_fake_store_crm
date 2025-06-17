CONTAINER_NAME := $(shell docker compose ps -q | head -n 1)
echo "Container Name: $(CONTAINER_NAME)"

test:
	docker exec -it $(CONTAINER_NAME) \
	pytest -v \
	--cov=marketbridge.services \
	--cov-report=term-missing

build:
	docker compose up --build -d

migrate:
	docker exec -it $(CONTAINER_NAME) \
	python manage.py makemigrations && \
	docker exec -it $(CONTAINER_NAME) \
	python manage.py migrate
	
psql:
	docker exec -it postgres_db psql \
	-U postgres \
	-d marketbridge_dev