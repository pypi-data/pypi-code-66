"""
    sphinxcontrib.direct-copy
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A sphinx extension to copy files directly from the source directory to the target
    directory. 

    :copyright: Copyright 2020 Nokia
    :license: Apache License 2.0, see LICENSE for details.
"""
import os as _os
from . import implementation as _impl

if False:
    # For type annotations
    from typing import Any, Dict  # noqa
    from sphinx.application import Sphinx  # noqa

def setup(app):

    app.connect('build-finished', _impl.readme_to_index)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }