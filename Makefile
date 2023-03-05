.PHONY: requirements help ufs flashit

help:
	@echo "requirements    install project requirements"
	@echo
	@echo "ufs              install microfs utility, required for flashing files"
	@echo "flashit          copy project to microbit"

venv:
	python3 -m venv venv

pip-upgrade: venv
	. venv/bin/activate && pip install --upgrade pip

requirements: pip-upgrade
	. venv/bin/activate && pip install -r requirements.txt

ufs:
	pip install microfs

flashit:
	ufs put src/main.py src/config.py
