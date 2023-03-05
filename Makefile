.PHONY: help ufs flashit

help:
	@echo "ufs              install microfs utility, required for flashing files"
	@echo "flashit          copy project to microbit"

ufs:
	pip install microfs

flashit:
	ufs put src/main.py src/config.py
