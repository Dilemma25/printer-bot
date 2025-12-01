##############
# Конфигурация

create-env:
	@cp ./.env.example ./.env

generate-req:
	@cd bot && poetry run pip freeze > requirements.txt

###########################################
# Управление контейнерами сервере

up:
	@docker compose up -d --build

down:
	@docker compose down

start:
	@docker compose start

stop:
	@docker compose stop

show-logs:
	@docker compose logs

follow-logs:
	@docker compose logs -f
