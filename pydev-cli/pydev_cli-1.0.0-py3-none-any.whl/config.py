import configparser
from pathlib import Path
from typing import Optional

from pydantic import BaseSettings

from .utils import get_current_project_name


class PydevCLISettings(BaseSettings):
    """Configuration for pydev-cli."""

    package_name: Optional[str] = None
    src_dir: Path = Path("src")
    tests_dir: Path = Path("tests")
    dist_dir: Path = Path("dist")
    docs_dir: Path = Path("docs")
    app_import: Optional[str] = None
    docker_image: Optional[str] = None
    docker_tag: str = "latest"
    docker_namespace: str = "gcharbon"


def load_config() -> PydevCLISettings:
    """Load config from setup.cfg or environment variables.

    Returns:
        A PyDevCLISettings instance holding all configuration.
    """
    config = configparser.ConfigParser()
    try:
        config.read("setup.cfg")
        settings = PydevCLISettings(**config["pydev-cli"])
    except (FileNotFoundError, KeyError):
        settings = PydevCLISettings()

    package_name = get_current_project_name()

    if settings.package_name is None:
        settings.package_name = package_name

    if settings.docker_image is None:
        settings.docker_image = settings.package_name

    if settings.app_import is None:
        settings.app_import = f"{settings.package_name}:app"

    return settings
