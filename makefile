DEV_COMPOSE := docker-compose.dev.yml
PROD_COMPOSE := docker-compose.yml

# start dev docker compose
.PHONY: devup
devup:
	docker-compose -f $(DEV_COMPOSE) up

# stop dev docker compose
.PHONY: devdown
devdown:
	docker-compose -f $(DEV_COMPOSE) down

# start prod docker compose
.PHONY: produp
produp:
	docker-compose -f $(PROD_COMPOSE) up

# stop prod docker compose
.PHONY: proddown
proddown:
	docker-compose -f $(PROD_COMPOSE) down
