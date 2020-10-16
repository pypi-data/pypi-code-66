from django.core.management.base import BaseCommand

from ...tasks import execute_housekeep_tasks


class Command(BaseCommand):

    def handle(self, *args, **options):
        execute_housekeep_tasks()
