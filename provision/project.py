from invoke import task

from . import common


##############################################################################
# Manage dependencies
##############################################################################
@task
def install_tools(context):
    """Install shell/cli dependencies, and tools needed to install requirements

    Define your dependencies here, for example
    local("sudo npm -g install ngrok")
    """
    context.run("pip install --upgrade setuptools pip pip-tools wheel")


@task
def install_requirements(context, env="production"):
    """Install local development requirements"""
    common.success(f"Install requirements with pip from {env}.txt")
    context.run(f"pip install -r requirements/{env}.txt")


@task
def pip_compile(context, update=False):
    """Compile requirements with pip-compile"""
    common.success("Compile requirements with pip-compile")
    upgrade = "-U" if update else ""
    in_files = [
        "requirements/production.in",
    ]
    for in_file in in_files:
        context.run(f"pip-compile -q {in_file} {upgrade}")
