from django.apps import AppConfig

class PathomationConfig(AppConfig):
    name = 'pathomation.apps.PathomationConfig'
    label = 'Pathomation_plugin'  # <-- this is the important line - change it to anything other than the default, which is the module name ('foo' in this case)


default_app_config = 'pathomation.apps.PathomationConfig'