APP = restapi-flask

.PHONY: build up down logs

compose:
	docker-compose build
	docker-compose up
down:
	docker-compose down
logs:
	docker-compose logs -f

test:
	black .
	flake8 . --exclude ./venv
	bandit -r . -x '/venv/','/tests/'
	pytest -v --disable-warnings