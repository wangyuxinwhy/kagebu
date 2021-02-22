# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

# How To Use

1. Step 0 准备开发环境
    - make create-env # 创建虚拟环境
    - make install # 安装常用的开发依赖
    - pre-commit install # 安装 pre-commit hooks
2. Step 1 使用以下提供的命令辅助开发
    ```shell script
    # install 3rd package
    poetry add <package_name>
    poetry add --dev <package_name>

    # export environment setting
    make export-env

    # foramt all python file
    make format

    # test 
    make test

    # lint code
    make lint
    ```
