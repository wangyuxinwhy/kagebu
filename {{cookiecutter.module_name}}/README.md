# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

```shell script
# use virtual env 使用 conda 来控制环境 poetry 代替 pip
make create-env

# install 3rd package
poetry add <package_name>
poetry add --dev <package_name>

# install all dependencies
make install

# export environment setting
make export-env

# foramt all python file
make format

# test 
make test

# lint code
make lint

# init docs
sphinx-quickstart
```
