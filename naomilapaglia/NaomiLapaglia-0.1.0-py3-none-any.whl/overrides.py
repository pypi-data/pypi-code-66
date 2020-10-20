from pathlib import Path
from shutil import copy
import argparse


def admin_override():
    parser = argparse.ArgumentParser(description='Naomi Lapaglia is python package used for overriding '
                                                 'admin logo, title and welcome message in Wagtail projects.')

    parser.add_argument('-l', metavar='label', default=0, nargs='?', type=str,
                        help='App name inside project where custom files and '
                             'templates for Wagtail admin site will be stored.')

    args = parser.parse_args()

    # Wagtail project paths
    project_path = Path().absolute()
    project_name = args.l if args.l else project_path.name
    project_images = Path.joinpath(project_path, f'{project_name}/static/images/')
    project_wagtailadmin = Path.joinpath(project_path, f'{project_name}/templates/wagtailadmin/')

    # NaomiLapaglia package paths
    package_path = Path(__file__).parent
    package_logo = Path.joinpath(package_path, 'static/images/publitzer_go_logo.svg')
    package_base_template = Path.joinpath(package_path, 'templates/base.html')
    package_admin_base_template = Path.joinpath(package_path, 'templates/admin_base.html')
    package_home_template = Path.joinpath(package_path, 'templates/home.html')

    # Create directories
    if not Path.is_dir(project_images):
        Path.mkdir(project_images)
    if not Path.is_dir(project_wagtailadmin):
        Path.mkdir(project_wagtailadmin)

    # Logo override
    copy(package_logo, project_images)
    copy(package_base_template, project_wagtailadmin)
    # Welcome override
    copy(package_home_template, project_wagtailadmin)
    # Title override
    copy(package_admin_base_template, project_wagtailadmin)
