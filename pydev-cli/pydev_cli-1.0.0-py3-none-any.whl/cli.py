"""This file define scripts that can be used during development."""
import os
from pathlib import Path

from typer import Argument, Option, Typer, echo

from .config import load_config
from .utils import exit, run

CONFIG = load_config()

SRC_FILES = " ".join([str(path) for path in CONFIG.src_dir.glob("**/*.py")])
TEST_FILES = " ".join([str(path) for path in CONFIG.tests_dir.glob("**/*.py")])


app = Typer(
    name="FastAPI development toolkit",
    no_args_is_help=True,
    help="A command line tool to automate most of development tasks.",
    add_completion=False,
)

services_app = Typer(
    name="Docker services toolkit",
    no_args_is_help=True,
    help="A group of command to manager docker services during development.",
    add_completion=False,
)

app.add_typer(services_app, name="services")


@app.command()
def dev(
    host: str = Option(
        "localhost", envvar="HOST", help="The host your application will listen to.",
    ),
    port: int = Option(
        8000, envvar="PORT", help="The port your application will listen to."
    ),
    reload: bool = Option(
        True,
        envvar="RELOAD",
        help="With hot-reload enabled, your application will restart on each file change.",
    ),
    debug: bool = Option(
        True, envvar="DEBUG", help="Start the application in debug mode."
    ),
) -> None:
    """Start the application in development mode."""
    if debug:
        os.environ["PYTHONASYNCIODEBUG"] = "1"
        os.environ["LOGGING_LEVEL"] = "DEBUG"
    try:
        import uvicorn
    except (ImportError, ModuleNotFoundError):
        exit(
            "Error: You must install uvicorn as a development dependency to use the 'dev' command. "
            "Use 'poetry add --dev uvicorn' to fix the problem."
        )
    uvicorn.run(CONFIG.app_import, reload=reload, host=host, port=port)


@app.command()
def docs(
    host: str = Option("localhost", help="Host documentation server will listen to."),
    port: int = Option(8080, help="Port the documentation server will listen to."),
) -> None:
    """Serve the documentation on development server."""
    cmd = f"mkdocs serve --dev-addr {host}:{port}"
    run(cmd)


@app.command()
def lint() -> None:
    """Perform linting using flake8."""
    cmd = f"flake8 {SRC_FILES} {TEST_FILES}"
    run(cmd)


@app.command()
def format() -> None:
    """Format the code using black and isort."""
    black_cmd = f"black {SRC_FILES} {TEST_FILES}"
    isort_cmd = f"isort {SRC_FILES} {TEST_FILES}"
    run(black_cmd)
    run(isort_cmd)


@app.command()
def test() -> None:
    """Run the tests using pytest."""
    os.environ["PYTHONASYNCIODEBUG"] = "1"
    os.environ["LOGGING_LEVEL"] = "DEBUG"
    os.environ["LOGGING_TEST_MODE"] = "1"
    cmd = "pytest"
    run(cmd)


@app.command()
def typecheck() -> None:
    """Run type checking using mypy."""
    cmd = f"mypy {CONFIG.src_dir} {CONFIG.tests_dir}"
    run(cmd)


@app.command()
def build(
    package: bool = Option(True, help="Build the python package in wheel format.",),
    docs: bool = Option(True, help="Build the documentation."),
    coverage: bool = Option(
        True, help="Run the unit tests before building documentation or package."
    ),
    verbose: bool = Option(False, help="Show python traceback if any task failed."),
) -> None:
    """Run tests, build documentation and built package."""
    if coverage:
        pytest_cmd = "pytest"
        if not Path(CONFIG.docs_dir / "coverage-report" / "index.html").is_file():
            echo("Running tests to generate coverage report.")
            run(pytest_cmd)
    if docs:
        mkdocs_cmd = f"mkdocs build -d {CONFIG.docs_dir}"
        run(mkdocs_cmd)
    if package:
        poetry_cmd = "poetry build"
        run(poetry_cmd, verbose=verbose)


@app.command()
def publish(repository: str = "pypi") -> None:
    """Publish package to external repository."""
    poetry_cmd = f"poetry publish --repository {repository}"
    run(poetry_cmd)


@app.command()
def release() -> None:
    """Bump version according to semver specification."""
    release_cmd = "semantic-release version"
    run(release_cmd)


@app.command()
def changelog() -> None:
    """Print the changelog to stdout."""
    changelog_cmd = "semantic-release changelog"
    run(changelog_cmd)


@app.command()
def build_docker_image(
    namespace: str = CONFIG.docker_namespace,
    image: str = CONFIG.docker_image,  # type: ignore
    tag: str = CONFIG.docker_tag,
) -> None:
    """Build the docker image for production usage."""
    docker_cmd = f"docker build -t {namespace}/{image}:{tag} -f docker/Dockerfile ."
    run(docker_cmd)


@app.command()
def build_ci_docker_image(
    namespace: str = CONFIG.docker_namespace,
    image: str = f"{CONFIG.docker_image}-ci",
    tag: str = "latest",
) -> None:
    """Build the docker image for continuous integration usage."""
    docker_cmd = f"docker build -t {namespace}/{image}:{tag} -f docker/Dockerfile ."
    run(docker_cmd)


@app.command()
def nb_kernel(
    display_name: str = Argument(
        CONFIG.package_name, help="Displayed name for the kernel."
    )
) -> None:
    """Create an IPython kernel to use with jupyter notebook."""
    try:
        import ipykernel as _  # noqa: F401
    except ModuleNotFoundError:
        run("poetry add --dev ipykernel")
    run(
        "python -m ipykernel install --user"
        f' --name "{CONFIG.package_name}"'
        f' --display-name "{display_name}"'
    )


@services_app.command()
def start(local: bool = True, app: bool = False) -> None:
    """Start a service."""
    if local:
        run(
            "docker stack deploy "
            f"{'-c compose/docker-compose.yml ' if app else ''}"
            "-c compose/docker-compose.dependencies.yml "
            "-c compose/docker-compose.local.yml "
            f"local-{CONFIG.package_name}"
        )
    else:
        run(
            "docker stack deploy "
            f"{'-c compose/docker-compose.yml ' if app else ''}"
            "-c compose/docker-compose.dependencies.yml "
            "-c compose/docker-compose.traefik.yml"
            f"dev-{CONFIG.package_name}"
        )


@services_app.command()
def stop(local: bool = True) -> None:
    """Stop a service."""
    if local:
        run(f"docker stack rm local-{CONFIG.package_name}")
    else:
        run(f"docker stack rm dev-{CONFIG.package_name}")
