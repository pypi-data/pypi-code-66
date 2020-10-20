from pathlib import Path
from shutil import copy
CUSTOMIZE = [
    # base.html
    'wagtail_logo',
    # home.html
    'wagtail_welcome',
    # admin_base.html
    'wagtail_favicon'
]

def admin_override():
    """
        Project paths
    """
    project_path = Path().absolute()
    project_name = project_path.name
    project_images = Path.joinpath(project_path, f'{project_name}/static/images/')
    project_wagtailadmin = Path.joinpath(project_path, f'{project_name}/templates/wagtailadmin/')
    """
        Package paths
    """
    package_path = Path(__file__).parent
    package_image_path = Path.joinpath(package_path,
                                       'static/images/publitzer_go_logo.svg')
    package_base_path = Path.joinpath(package_path, 'templates/base.html')
    package_admin_base_path = Path.joinpath(package_path, 'templates/admin_base.html')
    package_home_path = Path.joinpath(package_path, 'templates/home.html')

    # Create directories
    if not Path.is_dir(project_images):
        Path.mkdir(project_images)
    if not Path.is_dir(project_wagtailadmin):
        Path.mkdir(project_wagtailadmin)

    # Logo
    copy(package_image_path, project_images)
    copy(package_base_path, project_wagtailadmin)
    # Welcome
    copy(package_home_path, project_wagtailadmin)
    # Favicon
    copy(package_admin_base_path, project_wagtailadmin)
    print("Done")
