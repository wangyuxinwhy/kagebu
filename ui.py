# -*- coding: utf-8 -*-
import io
import json
import subprocess
from pathlib import Path
from tempfile import NamedTemporaryFile

import streamlit as st
from cookiecutter.main import cookiecutter


st.subheader("Meta info")
col1, col2 = st.beta_columns(2)
full_name = col1.text_input("full_name", "wangyuxin")
email = col2.text_input("email", "yuxin_wang_94@163.com")
st.subheader("Project info")
col21, col22, col23 = st.beta_columns(3)
project_name = col21.text_input("project_name", "Python Project Name")
project_slug = col22.text_input("project_slug", project_name.lower().replace(' ', '_').replace('-', '_'))
module_name = col23.text_input("module_name", project_slug)
project_short_description = st.text_area("project_short_description", "description...")
col31, col32 = st.beta_columns(2)
python_version = col31.text_input("python_version", "^3.6.8")
open_source_license = col32.selectbox("license", ["Not open source", "MIT license", "BSD license", "ISC license", "Apache Software License 2.0", "GNU General Public License v3"])
st.subheader("Extra Options")
command_line_interface = st.checkbox("Command Line Interface")

info = {
    "full_name": full_name,
    "email": email,
    "project_name": project_name,
    "project_short_description": project_short_description,
    "project_slug": project_slug,
    "module_name": module_name,
    "python_version": python_version,
    "command_line_interface": command_line_interface,
    "open_source_license": open_source_license
}

st.subheader("Preview")
st.write(info)

st.subheader("Create Project")
project_root_dir = st.text_input("输入 Project Root Dir:", str(Path.home().resolve()))
if st.button("Create"):
    temp_file = NamedTemporaryFile()
    with open(temp_file.name, "w") as f:
        f.write(json.dumps(info))
    cookiecutter(".", config_file=temp_file.name)
