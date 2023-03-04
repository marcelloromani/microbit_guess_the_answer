.PHONY: requirements help

help:
	@echo "requirements    install project requirements"

venv:
	python3 -m venv venv

pip-upgrade: venv
	. venv/bin/activate && pip install --upgrade pip

requirements: pip-upgrade
	. venv/bin/activate && pip install -r requirements.txt
