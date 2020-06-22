.PHONY: help
help:
	@echo "Usage: make [COMMAND] [ARGS]..."
	@echo ""
	@echo "  This makefile is a collection of usefull commands to interact with python-test-fun."
	@echo ""
	@echo "Commands:"
	@echo ""
	@echo "  help                   Show this message and exit."
	@echo ""
	@echo "  venv                   Install a Python virtualenv and all required libraries."
	@echo ""
	@echo "  run_tests              Run tests."

.PHONY: venv
venv:
	python3 -m virtualenv -p python3 venv
	venv/bin/pip install -r requirements.txt

.PHONY: run_tests
run_tests:
	PYTHONPATH=. venv/bin/python tests/sandbox/test_hello_world.py
