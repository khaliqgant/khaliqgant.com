.PHONY: tests
tests :
		python -m unittest discover -s tests -p '*_Test.py'
