VIRTUAL_ENV = .venv

.PHONY: all
all: install run

.PHONY: run
run:
	$(VIRTUAL_ENV)/bin/python manage.py runserver

.PHONY: install
install:
	python3 -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/pip install -r requirements.txt
	npm install bootstrap@^5.0.0
	$(VIRTUAL_ENV)/bin/python manage.py migrate
	$(VIRTUAL_ENV)/bin/python manage.py loaddata data.json
	$(VIRTUAL_ENV)/bin/python manage.py populate
