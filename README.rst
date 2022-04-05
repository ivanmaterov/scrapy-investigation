====================
scrapy-investigation
====================


.. image:: https://img.shields.io/pypi/v/scrapy_investigation.svg
        :target: https://pypi.python.org/pypi/scrapy_investigation

.. image:: https://img.shields.io/travis/ivanmaterov/scrapy_investigation.svg
        :target: https://travis-ci.com/ivanmaterov/scrapy_investigation

.. image:: https://readthedocs.org/projects/scrapy-investigation/badge/?version=latest
        :target: https://scrapy-investigation.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A small project for scrapy-investigation


* Free software: BSD license

Install project
---------------

You have to have the following tools installed prior initializing the project:

- pyenv_
- pyenv-virtualenv_

.. _pyenv: https://github.com/pyenv/pyenv
.. _pyenv-virtualenv: https://github.com/pyenv/pyenv-virtualenv

*Prepare the project*

1. Create separate python virtual environment

``
pyenv install 3.9.8
pyenv virtualenv 3.9.8 scrapy-investigation
pyenv local scrapy-investigation
pyenv activate scrapy-investigation
``

2. Set up packages for using `invoke`

``
pip install -r requirements/local_build.txt
inv project.install-requirements
``

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
