# -*- coding: utf-8 -*-
import re
import subprocess
from pathlib import Path

import streamlit as st
from cookiecutter.generate import generate_files
from conda.base.context import context
from conda.core.envs_manager import list_all_known_prefixes


def get_python_version_from_env_path(env_path):
    binary_path = str(Path(env_path) / "bin" / "python")
    sub_result = subprocess.run([binary_path, "--version"], capture_output=True)
    output = sub_result.stdout.decode("utf-8") + sub_result.stderr.decode("utf-8")
    finds = re.findall(r'[Pp]ython\s?([23]\.\d{1,2})\.\d{1,2}', output)
    if finds:
        return finds[0]
    else:
        raise Exception("不能正确的获得 python 版本")


st.subheader("Meta info")
col1, col2 = st.beta_columns(2)
full_name = col1.text_input("full_name", "wangyuxin")
email = col2.text_input("email", "yuxin_wang_94@163.com")
st.subheader("Project info")
col21, col22, col23 = st.beta_columns(3)
project_name = col21.text_input("project_name", "Python Project Name")
module_name = col22.text_input("module_name", project_name.lower().replace(' ', '_').replace('-', '_'))
open_source_license = col23.selectbox("license", ["Not open source", "MIT license", "BSD license", "ISC license", "Apache Software License 2.0", "GNU General Public License v3"])
project_short_description = st.text_area("project_short_description", "description...")
st.subheader("Extra Options")
command_line_interface = st.checkbox("Command Line Interface")

st.subheader("Choose Virtual Envs")
conda_env_paths = list_all_known_prefixes()
use_new = st.checkbox("Use New Virtual Environment", False)
if use_new:
    col41, col42 = st.beta_columns(2)
    with col41:
        new_env_name = st.text_input("Env Name")
    with col42:
        python_version = st.selectbox("Python Version", ["2.7", "3.6", "3.7", "3.8"], index=1)
    conda_env_path = str(Path(context.envs_dirs[0]) / new_env_name)
else:
    conda_env_path = st.selectbox("Conda Envs", conda_env_paths)
    python_version = get_python_version_from_env_path(conda_env_path)

st.subheader("Preview")
info = {
    "full_name": full_name,
    "email": email,
    "project_name": project_name,
    "project_short_description": project_short_description,
    "project_slug": module_name,
    "module_name": module_name,
    "conda_env_path": conda_env_path,
    "python_version": "^" + python_version,
    "command_line_interface": command_line_interface,
    "open_source_license": open_source_license
}
st.write(info)

st.subheader("Create Project")
project_root_dir = st.text_input("输入 Project Root Dir:", str(Path.home().resolve() / "workspace"))
if st.button("Create"):
    if use_new:
        subprocess.run(["conda", "create", "-n", new_env_name, f"python={python_version}"])
    context = {"cookiecutter": info}
    kagebu_dir = Path(".").resolve()
    context['cookiecutter']['_template'] = kagebu_dir
    result = generate_files(
        kagebu_dir,
        context=context,
        output_dir=project_root_dir,
    )
    st.write(f"create project in {result}")
