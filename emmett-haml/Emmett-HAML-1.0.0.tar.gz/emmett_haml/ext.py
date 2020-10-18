# -*- coding: utf-8 -*-
"""
    emmett_haml.ext
    ---------------

    Provides the HAML extension for Emmett

    :copyright: 2017 Giovanni Barillari
    :license: BSD-3-Clause
"""

import os

from emmett.extensions import Extension
from renoir_haml import Haml as RenoirHaml


class Haml(Extension):
    default_config = dict(
        set_as_default=False,
        preload=True,
        encoding='utf8',
        auto_reload=False
    )

    def on_load(self):
        ext = self.app.use_template_extension(
            RenoirHaml,
            encoding=self.config.encoding,
            reload=self.config.auto_reload
        )
        if self.config.set_as_default:
            self.app.template_default_extension = '.haml'
        if not self.config.preload:
            return
        for path, dirs, files in os.walk(self.app.template_path):
            for fname in files:
                if os.path.splitext(fname)[1] == ".haml":
                    file_path = os.path.join(path, fname)
                    rel_path = file_path.split(self.app.template_path + "/")[1]
                    ext._build_html(os.path.join(path, fname), rel_path)
