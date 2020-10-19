from django.apps import AppConfig
from django.apps import apps
from django.conf import settings

class DjangoEveOnlineDoctrineManagerConfig(AppConfig):
    name = 'django_eveonline_doctrine_manager'
    package_name = __import__(name).__package_name__
    version = __import__(name).__version__
    verbose_name = "EVE Doctrine Manager"
    url_slug = 'eveonline'
    install_requires = ['crispy_forms', 'django_eveonline_connector']

    def ready(self):
        for requirement in self.install_requires:
            if requirement not in settings.INSTALLED_APPS:
                raise Exception(f"Missing '{requirement}' in INSTALLED_APPS")

        if apps.is_installed('packagebinder'):
            from packagebinder.bind import BindObject
            bind = BindObject(self.package_name, self.version)
            # Required Task Bindings
            bind.add_required_task(
                name="EVE: Generate Doctrine Reports",
                task="django_eveonline_doctrine_manager.tasks.update_character_reports",
                interval=1,
                interval_period="days",
            )
            bind.save()
