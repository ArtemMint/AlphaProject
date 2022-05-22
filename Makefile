init: up update-db
reboot: down up
up: docker-build docker-up docker-prune
down: docker-down
update-db: docker-migrations docker-migrate
collect_static: docker-collect_static

docker-build:
	cd docker && docker-compose build
docker-up:
	cd docker && docker-compose up
docker-down:
	cd docker && docker-compose down
docker-stop:
	cd docker && docker-compose stop
docker-prune:
	cd docker && docker image prune -f
docker-migrations:
	cd docker && docker-compose exec django ./manage.py makemigrations --no-input
docker-migrate:
	cd docker && docker-compose exec django ./manage.py migrate --no-input
docker-shell:
	cd docker && docker-compose exec django ./manage.py shell
docker-collect_static:
	cd docker && docker-compose exec django ./manage.py collectstatic --no-input