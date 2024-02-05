SETPY=PYTHONPATH=app/

fmt:
	poetry run ruff format app tests
	poetry run ruff check app tests --fix
	poetry run toml-sort pyproject.toml

lint:
	poetry run ruff format --check app tests
	poetry run ruff check app tests
	poetry run mypy app
	poetry run toml-sort pyproject.toml --check
	poetry run pymarkdown scan README.md

test:
	poetry run pytest --dead-fixtures
	poetry run pytest

server:
	$(SETPY) poetry run uvicorn app.main:app --reload

migration:
	$(SETPY) alembic revision --autogenerate -m $(name)

migrate:
	$(SETPY) alembic upgrade head
