import asyncio
import json
from pathlib import Path

from cleo import Command

import isilon


class ObjectsCommand(Command):
    """
    Objects.

    objects
        {container : Container name.}
        {object : Object name.}
        {--headers=* : HTTP headers.}
        {--data=? : Object data.}
        {--c|create : Create or replace object.}
        {--m|metadata : Show object metadata.}
        {--u|update : Create or update object metadata.}
        {--d|delete : Delete object.}
    """

    def handle(self):
        container_name = str(self.argument("container"))
        object_name = str(self.argument("object"))
        headers = dict()
        for header in self.option("headers"):
            headers.update(json.loads(header))
        if self.option("create"):
            try:
                data = Path(self.option("data"))
            except TypeError:
                self.line("<error>Please, provides a valid object.</>")
                raise SystemExit(1)
            if not data.is_file():
                self.line("<error>Please, provides a valid object.</>")
                raise SystemExit(1)
            asyncio.run(
                isilon.objects.create_large(
                    container_name, object_name, data, headers=headers
                )
            )
            self.line(
                f"<options=bold><comment>{object_name}</comment> object created.</>"
            )
        elif self.option("metadata"):
            resp = asyncio.run(
                isilon.objects.show_metadata(
                    container_name, object_name, headers=headers
                )
            )
            for meta_key, meta_value in resp.items():
                self.line(f"<options=bold>{meta_key}</>: {meta_value}")
        elif self.option("update"):
            asyncio.run(
                isilon.objects.update_metadata(
                    container_name, object_name, headers=headers
                )
            )
            self.line("<options=bold>metadata updated.</>")
        elif self.option("delete"):
            asyncio.run(
                isilon.objects.delete(container_name, object_name, headers=headers)
            )
            self.line(
                f"<options=bold><comment>{object_name}</comment> object deleted.</>"
            )
        else:
            asyncio.run(
                isilon.objects.get_large(
                    container_name, object_name, object_name, headers=headers
                )
            )
            self.line(
                f"<options=bold><comment>{object_name}</comment> object saved.</>"
            )
