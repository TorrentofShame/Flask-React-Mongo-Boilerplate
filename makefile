DEV_COMPOSE := docker-compose.dev.yml
PROD_COMPOSE := docker-compose.yml
KUBE_DIR := kube-config

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

# Build production images
.PHONY: build
build:
	docker-compose -d -f $(PROD_COMPOSE) build

# Create Kube Containers
.PHONY: kubecreate
kubecreate: | build
	kubectl create -f $(KUBE_DIR)

# Delete Kube Containers
.PHONY: kubedelete
kubedelete:
	kubectl delete -f $(KUBE_DIR)

