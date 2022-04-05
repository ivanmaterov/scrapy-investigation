# Installing project for developing on local PC

You have to have the following tools installed prior initializing the project:

- [pyenv](https://github.com/pyenv/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

# Prepare the project

1. Create separate python virtual environment

```bash
pyenv install 3.9.8
pyenv virtualenv 3.9.8 scrapy-investigation
pyenv local scrapy-investigation
pyenv activate scrapy-investigation
```

2. Set up packages for using `invoke`

```bash
pip install -r requirements/local_build.txt
inv project.install-requirements
```
