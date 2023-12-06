# Software tools that we use and like

This document is a list of software that we like and want to share.

Feel free to edit the document to add your favourite tool or add more details
about the ones here!

## Python environment and dependency management tools

* [pyenv](https://github.com/pyenv/pyenv) is useful for installing and managing
Python versions.

* [venv](https://docs.python.org/3/library/venv.html) is Python's built-in tool
for virtual environments.

* [poetry](https://python-poetry.org/),
[pipenv](https://pipenv.pypa.io/en/latest/) and
[pdm](https://pdm.fming.dev/latest/) are Python dependency managers.

* [conda](https://docs.conda.io/en/latest/) is a package management system that
aims to address all your scientific programming needs, in Python and beyond.

* [pixi](https://prefix.dev/docs/pixi/overview) is a new alternative interface
for installing conda packages (and soon also packages from PyPI).

## Project templates

* [cookiecutter](https://pypi.org/project/cookiecutter/) is an application that
lets you easily download a custom template to start your project with.

* [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)
is a skeleton data science project.

* [cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python)
is a template for a Python package that uses recent tooling and conventions.

* [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
is a more traditional Python package template.

* [cookiecutter-cms](https://github.com/MolSSI/cookiecutter-cms) is a template
that specifically targets computational molecuar science

* [bibat](https://bibat.readthedocs.io/en/latest/) is a template for Bayesian
statistical analysis projects.

## Code checkers and formatters

* [isort](https://pre-commit.com/) checks that your Python imports are idiomatic.

* [ruff](https://beta.ruff.rs/docs/) checks for and can sometimes correct common
Python mistakes.

* [black](https://github.com/psf/black) formats your code: never worry about
indentation again!

* [pre-commit](https://pre-commit.com/) can run your checkers and formatters as
pre-commit hooks.

## Documentation

* [Sphinx](https://www.sphinx-doc.org/en/master/) is the de facto standard for
generating Python documentation from source code docstrings.

* [MyST](https://myst-parser.readthedocs.io/en/v0.15.1/sphinx/intro.html) lets
you write Sphinx documentation in Markdown instead of reStructuredText.

* [readthedocs](https://about.readthedocs.com/?ref=readthedocs.org) builds and
hosts your documentation for free.

## Dataframes

* [Pola.rs](https://www.pola.rs/) is a dataframe library. It's often faster or
smarter about memory management than pandas.

## Shell

* [Slime](https://en.wikipedia.org/wiki/SLIME) and
[vim-slime](https://github.com/jpalardy/vim-slime) let you easily send code to
a REPL from pretty much anywhere.

* [Warp](https://www.warp.dev/) is a featureful terminal application for macos.

## Dashboards

* [Streamlit](https://streamlit.io/) makes it easy to share data science work
  online using a minimal, script-oriented Python webapp framework.

  Best feature: Streamlit will deploy and host your webapp for free.

* [Dash](https://dash.plotly.com/) is a dashboarding tool for
[plotly](https://plotly.com/) plots.

* [Shiny](https://shiny.posit.co/) is a dashboarding tool that is extremely
popular in the R world and is also a Python package.

## Misc

* [Mojo](https://www.modular.com/mojo) is a language that extends Python with
systems programming features, with the aim to remove the need for numerical
Python libraries to interface with specialised systems programming languages.
