""" A simple command line interface wrapper around cookiecutter which uses the template defined in this project. """
import json
from pathlib import Path
import sys

from typer import Typer, Context, echo
from pyfiglet import Figlet

from cookiecutter.main import cookiecutter


TEMPLATES_DIRECTORY = Path(__file__).parent / "templates"


app = Typer()


@app.command(
        context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def generate(
    ctx: Context,
    template: str = "default",
    overwrite: bool = False,
    data: str = None,
    no_input: bool = False
):
    """ Generate a new project using given template """
    if data:
        kwargs = json.loads(Path(data).read_text())
    else:
        kwargs = {}
    is_key = True
    for extra_arg in ctx.args:
        if is_key:
            key = extra_arg
            if key.startswith("--"):
                key = key[2:]
            elif key.startswith("-"):
                key = key[1:]
            is_key = False
            continue
        kwargs[key] = extra_arg
        is_key = True
    template_path = TEMPLATES_DIRECTORY / template
    if not template_path.is_dir():
        echo(f"Template not found: {template}", file=sys.stderr)
        sys.exit(1)
    echo(f"Creating new project using fastrepo {template} template.\n")
    cookiecutter(
        str(template_path),
        overwrite_if_exists=overwrite,
        extra_context=kwargs,
        no_input=no_input
    )
    f = Figlet(font='slant')
    echo("\n")
    echo(f.renderText('Fastrepo'))
    echo("""
    Learn more by reading the documentation at: https://gu-charbon.gitbook.io/fastrepo/.

    Do not forget to enable your environment before starting to develop:

        $ poetry shell

    Once you activated your environment, you can use the following command to list all available tasks:

        $ inv --list
    Or
        $ poetry run inv --list

    If you did not activate your environment.

    Happy coding!
    """)
