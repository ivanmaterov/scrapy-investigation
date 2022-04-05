from invoke import Exit, UnexpectedExit, task

from . import common

##############################################################################
# Linters
##############################################################################

DEFAULT_FOLDERS = "scrapy_investigation provision tasks.py"


@task
def isort(context, path=DEFAULT_FOLDERS, params=""):
    """Command to fix imports formatting."""
    common.success("Linters: ISort running")
    return context.run(command=f"isort {path} {params}")


@task
def isort_check(context, path=DEFAULT_FOLDERS):
    """Command to fix imports formatting."""
    return isort(context, path=path, params="--check-only")


@task
def pylint(context, path=DEFAULT_FOLDERS):
    """Run `pylint` linter."""
    common.success("Linters: PyLint running")
    return context.run(command=f"pylint {path}")


@task
def flake8(context, path=DEFAULT_FOLDERS):
    """Run `flake8` linter."""
    common.success("Linters: Flake8 running")
    return context.run(command=f"flake8 {path}")


# pylint: disable=redefined-builtin
@task
def all(context, path=DEFAULT_FOLDERS):
    """Run all linters"""
    common.success("Linters: running all linters")
    linters = (isort_check, flake8, pylint)
    failed = []
    for linter in linters:
        try:
            linter(context, path)
        except UnexpectedExit:
            failed.append(linter.__name__)
    if failed:
        common.error(
            f"Linters failed: {', '.join(map(str.capitalize, failed))}",
        )
        raise Exit(code=1)
