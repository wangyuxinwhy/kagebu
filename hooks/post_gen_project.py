#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


# def get_conda_python():
#     conda_env_path = "{{cookiecutter.conda_env_path}}"
#     return conda_env_path + "/bin/python"


if __name__ == "__main__":
    if "n" in "{{ cookiecutter.command_line_interface|lower}}":
        cli_file = os.path.join("{{ cookiecutter.module_name }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")
