# Kagebu
python 项目模板基于 cookiecutter、poetry、typer & conda。

- 使用 miniconda 做 Python 版本和虚拟环境的管理
- 使用 poetry 做依赖和 build、publish 的管理。
- 使用 typer 做命令行工具
- 使用 cookiecutter 做项目模板管理
- 使用 streamlit 提供 ui 界面

## Usage

### 通过 streamlit 提供的界面生成项目

1. 安装 poetry, [How to install poetry?](https://python-poetry.org/docs/#installation) 千万不要通过 pip 安装
2. 安装 conda, 推荐安装 miniconda
3. 安装此项目的依赖
```shell script
# 在 conda base 的虚拟环境下运行
poetry install
```
4. 启动 streamlit
```shell script
streamlit run ui.py
```

### 通过 cookiecutter

```shell script
cookiecutter gh:wangyuxinwhy/kagebu
```