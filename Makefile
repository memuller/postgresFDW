.PHONY: all

freeze:
	pip freeze > requirements.txt
deps:
	pip install -r requirements.txt

install:
	sudo python setup.py install

postgres:
	sudo -u postgres psql

prepare:
	psql -Upostgres -hlocalhost -f prepare.sql

console:
	python -ic "from model import *"

setup: install prepare
	sudo service postgresql restart

test: setup
	sudo -u postgres psql -c "SELECT * FROM wikipedia_pt WHERE title ~~ 'Robô'"