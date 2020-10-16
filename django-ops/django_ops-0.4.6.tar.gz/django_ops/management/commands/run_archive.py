import os

from django.core.management.base import BaseCommand

from ...models import ArchiveTask


class Command(BaseCommand):

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        root = "archived"
        if not os.path.exists(root):
            os.mkdir(root)
        is_delete = False
        if options['delete']:
            is_delete = True
        for task in ArchiveTask.objects.filter(enabled=True):
            task.run(root=root, is_delete=is_delete)
        print(is_delete)
