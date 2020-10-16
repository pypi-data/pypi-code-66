# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""A decorator which builds a :class:azure.ml.component.Component."""

from .component import component
from .pipeline import pipeline

__all__ = [
    'component',
    'pipeline',
]
