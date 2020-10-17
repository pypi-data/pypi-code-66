try:
    from gi.repository import GLib
    GLIB_AVAILABLE = True
except (ImportError, ValueError):
    GLIB_AVAILABLE = False

import openpaperwork_core

from . import deps


class Plugin(openpaperwork_core.PluginBase):
    PRIORITY = 1000

    def get_interfaces(self):
        return [
            "chkdeps",
            # "i18n",  # partial only
        ]

    def chkdeps(self, out: dict):
        if not GLIB_AVAILABLE:
            out['glib'].update(deps.GLIB)

    def i18n_date_long_month(self, date):
        dt = GLib.DateTime.new_utc(
            year=1999, month=date.month, day=2,
            hour=2, minute=2, seconds=2.0
        )
        return dt.format("%0b")
