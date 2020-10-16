import asyncio

from django.core.management.base import BaseCommand

from ...share import checker
from ...routines import HouseKeepRoutine, ArchiveRoutine


class Command(BaseCommand):

    def handle(self, *args, **options):
        loop = asyncio.get_event_loop()
        loop.create_task(HouseKeepRoutine().run_forever())
        loop.create_task(ArchiveRoutine().run_forever())
        loop.create_task(checker())
        loop.run_forever()
