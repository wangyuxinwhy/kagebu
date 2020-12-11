"""Console script for {{cookiecutter.project_slug}}."""
import typer

app = typer.Typer()


@app.command("hello")
def hello():
    print("Welcome to {{cookiecutter.project_name}}")


if __name__ == "__main__":
    app()
