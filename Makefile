.DEFAULT_GOAL := help

.PHONY: run-app
run-app: ## Run app with docker
	docker-compose up

.PHONY: re-build
re-build: ## Rebuild app and run app
	docker-compose up --build

.PHONY: stop-app
stop-app: ## Stop app
	docker-compose down

.PHONY: run-tests
run-tests: ## Run tests
	docker-compose run web python manage.py test app/leboncoin

.PHONY: run-migrations
run-migrations: ## Run migrations
	docker-compose exec web python manage.py makemigrations $(app)
	docker-compose exec web python manage.py migrate

.PHONY: run-console
run-console: ## Run console
	docker-compose run web python manage.py shell

.PHONY: run-pylint
run-pylint: ## Run linter
	docker-compose run web pylint --rcfile=pylintrc app/*/*.py


.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
