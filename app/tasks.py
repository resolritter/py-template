from typing import Any, Union


def typecheck():
    import os
    import subprocess
    import typing

    import tomlkit

    project_root = os.path.dirname(os.path.dirname(__file__))

    pyproject_toml_path = os.path.join(project_root, "pyproject.toml")
    pyproject_toml_fd = open(pyproject_toml_path, "r")
    pyproject_toml = typing.cast(
        dict[Any, Any], tomlkit.load(pyproject_toml_fd)
    )
    pyproject_toml_fd.close()

    project_name: str = pyproject_toml["tool"]["poetry"]["name"]
    result = subprocess.run(["mypy", "-p", project_name], cwd=project_root)

    exit(result.returncode)
