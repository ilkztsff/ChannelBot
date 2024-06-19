build:
	poetry run docker-compose build

up:
	poetry run docker-compose up --force-recreate --remove-orphans -d

start:
	poetry run docker-compose up --force-recreate --remove-orphans

stop:
	poetry run docker-compose stop

rm:
	poetry run docker-compose rm
	sudo rm -rf db

update:
	poetry update

lint:
	poetry run flake8
	poetry run mypy -p channelbot
