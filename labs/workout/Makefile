run:
	@uvicorn workout_api.main:app --reload

.PHONY: test

debug:
	@echo PYTHONPATH: $$PYTHONPATH
	@echo PWD: $(shell pwd)

test:
	@echo "Runing tests"

create-migrations:
	@export PYTHONPATH=$$PYTHONPATH:$(shell pwd) && alembic revision --autogenerate -m "$(d)"

run-migrations:
	@bash -c 'export PYTHONPATH=$$PYTHONPATH:$(shell pwd) && alembic upgrade head'