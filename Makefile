.PHONY: tests
tests :
		python -m unittest discover -s tests -p '*_Test.py'

.PHONY: init
init: venv/bin/activate
venv/bin/activate: requirements/dev.txt
	test -d venv || virtualenv venv
	venv/bin/pip install -Ur requirements/dev.txt
	touch venv/bin/activate

.PHONY: deps
deps:
	pip install -r requirements/dev.txt
