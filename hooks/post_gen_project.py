#!/usr/bin/env python
import os
import sys
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def get_conda_env_name():
    python_version = "{{cookiecutter.python_version}}"
    version = ""
    for i in python_version:
        if i in "0123456789":
            version += i
    return "py" + version[:2]


if __name__ == "__main__":
    try:
        from conda.core.envs_manager import list_all_known_prefixes
    except ImportError:
        print("========= ERROR =========")
        print("install miniconda for managing python version")
        print("========= ERROR =========")
        sys.exit(1)

    if "n" in "{{ cookiecutter.command_line_interface|lower}}":
        cli_file = os.path.join("{{ cookiecutter.module_name }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    target_env_name = get_conda_env_name()
    for n in list_all_known_prefixes():
        env_name = n.rsplit("/", 1)[-1]
        if env_name == target_env_name:
            subprocess.run(["poetry", "env", "use", f"{n}/bin/python"])
            break
    else:
        print("========= ERROR =========")
        print(
            f"Can not find matched conda env, install it, use:\nconda create -n {target_env_name} python={target_env_name[-2]}.{target_env_name[-1]}"
        )
        print("========= ERROR =========")
        sys.exit(1)
