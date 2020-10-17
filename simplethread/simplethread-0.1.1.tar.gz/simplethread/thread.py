# -*- coding: utf-8 -*-

"""
Drop-in replacement for the ``thread`` module.
"""

__all__ = ("allocate", "start_new")

from _thread import allocate_lock as allocate, start_new_thread as start_new
