from invoke import Collection

from provision import linters, project

ns = Collection(
    linters,
    project,
)

# Configurations for run command
ns.configure(
    dict(
        run=dict(
            pty=True,
            echo=True,
        ),
    ),
)
