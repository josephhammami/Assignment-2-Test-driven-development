#!/usr/bin/env make

# Change this to be your variant of the python command
PYTHON ?= python # python3 py

all:


# ---------------------------------------------------------
# Setup a venv and install packages.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc: clean
	@$(call MESSAGE,$@)
	rm -rf doc

clean-all: clean clean-doc
	@$(call MESSAGE,$@)
	rm -rf .venv


# ---------------------------------------------------------
# Code linters
#
pylint:
	@$(call MESSAGE,$@)
	-pylint *.py

flake8:
	@$(call MESSAGE,$@)
	-flake8

lint: flake8 pylint


# ---------------------------------------------------------
# Unit test and code coverage.
#
unittest:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m unittest discover

coverage:
	@$(call MESSAGE,$@)
	coverage run -m unittest discover
	coverage html
	coverage report -m

test: lint coverage


# ---------------------------------------------------------
# Generating documentation.
#
.PHONY: pydoc
pydoc:
	@$(call MESSAGE,$@)
	# This does not work on Windows installed Python
	$(PYTHON) -m pydoc -w "$(PWD)"
	install -d doc/pydoc
	mv *.html doc/pydoc

pdoc:
	@$(call MESSAGE,$@)
	pdoc --force --html --output-dir doc/pdoc *.py

pyreverse:
	@$(call MESSAGE,$@)
	install -d doc/pyreverse
	pyreverse *.py
	dot -Tpng classes.dot -o doc/pyreverse/classes.png
	dot -Tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot

doc: pdoc pyreverse #pydoc sphinx
