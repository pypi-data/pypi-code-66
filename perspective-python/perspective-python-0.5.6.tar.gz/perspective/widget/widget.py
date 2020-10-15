################################################################################
#
# Copyright (c) 2019, the Perspective Authors.
#
# This file is part of the Perspective library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

import six
import logging
import numpy
import pandas
import json
from datetime import date, datetime
from functools import partial
from ipywidgets import Widget
from traitlets import observe, Unicode
from ..core.data import deconstruct_pandas
from ..core.exception import PerspectiveError
from ..libpsp import is_libpsp
from ..viewer import PerspectiveViewer
from ..core._version import major_minor_version


def _type_to_string(t):
    """Convert a type object to a string representing a Perspective-supported
    type.  Redefine here as we can't have any dependencies on libbinding in
    client mode.
    """
    if t in six.integer_types:
        return "integer"
    elif t is float:
        return "float"
    elif t is bool:
        return "boolean"
    elif t is date:
        return "date"
    elif t is datetime:
        return "datetime"
    elif t is six.binary_type or t is six.text_type:
        return "string"
    else:
        raise PerspectiveError(
            "Unsupported type `{0}` in schema - Perspective supports `int`, `float`, `bool`, `date`, `datetime`, and `str` (or `unicode`).".format(
                str(t)
            )
        )


def _serialize(data):
    # Attempt to serialize data and pass it to the front-end as JSON
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        for v in data.values():
            # serialize schema values to string
            if isinstance(v, type):
                return {k: _type_to_string(data[k]) for k in data}
            elif isinstance(v, numpy.ndarray):
                return {k: data[k].tolist() for k in data}
            else:
                return data
    elif isinstance(data, numpy.ndarray):
        # structured or record array
        if not isinstance(data.dtype.names, tuple):
            raise NotImplementedError(
                "Data should be dict of numpy.ndarray or a structured array."
            )
        columns = [data[col].tolist() for col in data.dtype.names]
        return dict(zip(data.dtype.names, columns))
    elif isinstance(data, pandas.DataFrame) or isinstance(data, pandas.Series):
        # Take flattened dataframe and make it serializable
        d = {}
        for name in data.columns:
            column = data[name]
            values = column.values
            # Timezone-aware datetime64 dtypes throw an exception when using
            # `numpy.issubdtype` - match strings here instead.
            str_dtype = str(column.dtype)
            if "datetime64" in str_dtype:
                # Convert all datetimes to string for serializing
                values = numpy.datetime_as_string(column.values, unit="ms")
            d[name] = values.tolist()
        return d
    else:
        raise NotImplementedError(
            "Cannot serialize a dataset of `{0}`.".format(str(type(data)))
        )


class _PerspectiveWidgetMessage(object):
    """A custom message that will be passed from the Python widget to the
    front-end.

    When creating new messages, use this class as it defines a concrete schema
    for the message and prevents loosely creating `dict` objects everywhere.
    Use `to_dict()` to obtain the message in a form that can be sent through
    IPyWidgets.
    """

    def __init__(self, msg_id, msg_type, msg_data):
        """Create a new PerspectiveWidgetMessage."""
        self.id = msg_id
        self.type = msg_type
        self.data = msg_data

    def to_dict(self):
        """Returns a dictionary representation of the message."""
        return {"id": self.id, "type": self.type, "data": self.data}


class PerspectiveWidget(Widget, PerspectiveViewer):
    """:class`~perspective.PerspectiveWidget` allows for Perspective to be used
    in the form of a JupyterLab IPython widget.

    Using `perspective.Table`, you can create a widget that extends the full
    functionality of `perspective-viewer`.  Changes on the viewer can be
    programatically set on the :class`~perspective.PerspectiveWidget` instance,
    and state is maintained across page refreshes.

    Examples:
        >>> from perspective import Table, PerspectiveWidget
        >>> data = {
        ...     "a": [1, 2, 3],
        ...     "b": [
        ...         "2019/07/11 7:30PM",
        ...         "2019/07/11 8:30PM",
        ...         "2019/07/11 9:30PM"
        ...     ]
        ... }
        >>> tbl = Table(data, index="a")
        >>> widget = PerspectiveWidget(
        ...     tbl,
        ...     row_pivots=["a"],
        ...     sort=[["b", "desc"]],
        ...     filter=[["a", ">", 1]]
        ... )
        >>> widget.sort
        [["b", "desc"]]
        >>> widget.sort.append(["a", "asc"])
        >>> widget.sort
        [["b", "desc"], ["a", "asc"]]
        >>> widget.update({"a": [4, 5]}) # Browser UI updates
    """

    # Required by ipywidgets for proper registration of the backend
    _model_name = Unicode("PerspectiveModel").tag(sync=True)
    _model_module = Unicode("@finos/perspective-jupyterlab").tag(sync=True)
    _model_module_version = Unicode("~{}".format(major_minor_version)).tag(sync=True)
    _view_name = Unicode("PerspectiveView").tag(sync=True)
    _view_module = Unicode("@finos/perspective-jupyterlab").tag(sync=True)
    _view_module_version = Unicode("~{}".format(major_minor_version)).tag(sync=True)

    def __init__(
        self,
        data,
        index=None,
        limit=None,
        server=False,
        client=not is_libpsp(),
        **kwargs
    ):
        """Initialize an instance of :class`~perspective.PerspectiveWidget`
        with the given table/data and viewer configuration.

        If a pivoted DataFrame or MultiIndex table is passed in, the widget
        preserves pivots and applies them.  See `PerspectiveViewer.__init__` for
        arguments that transform the view shown in the widget.

        Args:
            data (:obj:`Table`|:obj:`View`|:obj:`dict`|:obj:`list`|:obj:`pandas.DataFrame`|:obj:`bytes`|:obj:`str`): a
                `perspective.Table` instance, a `perspective.View` instance, or
                a dataset to be loaded in the widget.

        Keyword Arguments:
            index (:obj:`str`): A column name to be used as the primary key.
                Ignored if `server` is True.

            limit (:obj:`int`): A upper limit on the number of rows in the Table.
                Cannot be set at the same time as `index`, ignored if `server`
                is True.

            server (:obj:`bool`): Whether to run Perspective in "server-only"
                mode, where the front-end client does not have its own Table,
                and instead reads all data and operations from Python.

            client (:obj:`bool`):  If True, convert the dataset into an Apache Arrow
                binary and create the Table in Javascript using a copy of the
                data. Defaults to False.

            kwargs (:obj:`dict`): configuration options for the `PerspectiveViewer`,
                and `Table` constructor if `data` is a dataset.

        Examples:
            >>> widget = PerspectiveWidget(
            ...     {"a": [1, 2, 3]},
            ...     aggregates={"a": "avg"},
            ...     row_pivots=["a"],
            ...     sort=[["b", "desc"]],
            ...     filter=[["a", ">", 1]],
            ...     computed_columns=[{
            ...         "column": "sqrt(a)",
            ...         "computed_function_name": "sqrt",
            ...         "inputs": ["a"]
            ...     }])
        """
        self._displayed = False
        self.on_displayed(self._on_display)

        # Trigger special flow when receiving an ArrayBuffer/binary
        self._pending_binary = None

        # If `self.client` is True, the front-end `<perspective-viewer>` is
        # given a copy of the data serialized to JSON, and the Python kernel
        # does not create a `perspective.Table.`
        self.client = client

        # If `self.server` is True, the widget runs in server-only mode where
        # the front-end `<perspective-viewer>` does not create a Table, and
        # will proxy all operations back to the server.
        self.server = server

        # Pass table load options to the front-end, unless in server mode
        self._options = {}

        if self.client:
            # Cache calls to `update()` before the widget has been displayed.
            self._predisplay_update_cache = []

        if index is not None and limit is not None:
            raise PerspectiveError("Index and Limit cannot be set at the same time!")

        # Parse the dataset we pass in - if it's Pandas, preserve pivots
        if isinstance(data, pandas.DataFrame) or isinstance(data, pandas.Series):
            data, config = deconstruct_pandas(data)

            if config.get("row_pivots", None) and "row_pivots" not in kwargs:
                kwargs.update({"row_pivots": config["row_pivots"]})

            if config.get("column_pivots", None) and "column_pivots" not in kwargs:
                kwargs.update({"column_pivots": config["column_pivots"]})

            if config.get("columns", None) and "columns" not in kwargs:
                kwargs.update({"columns": config["columns"]})

        # Initialize the viewer
        super(PerspectiveWidget, self).__init__(**kwargs)

        # Handle messages from the the front end
        # `PerspectiveJupyterClient.send()`:
        # - The "data" value of the message should be a JSON-serialized string.
        # - Both `on_msg` and `@observe("value")` must be specified on the
        # handler for custom messages to be parsed by the Python widget.
        self.on_msg(self.handle_message)

        if self.client:
            if is_libpsp():
                from ..libpsp import Table

                if isinstance(data, Table):
                    raise PerspectiveError(
                        "Client mode PerspectiveWidget expects data or schema, not a `perspective.Table`!"
                    )

            if index is not None:
                self._options["index"] = index

            if limit is not None:
                self._options["limit"] = limit

            # cache self._data so creating multiple views don't reserialize the
            # same data
            if not hasattr(self, "_data") or self._data is None:
                self._data = _serialize(data)
        else:
            # If an empty dataset is provided, don't call `load()` and wait
            # for the user to call `load()`.
            if data is None:
                if index is not None or limit is not None:
                    raise PerspectiveError(
                        "Cannot initialize PerspectiveWidget `index` or `limit` without a Table, data, or schema!"
                    )
            else:
                if index is not None:
                    self._options.update({"index": index})

                if limit is not None:
                    self._options.update({"limit": limit})

                self.load(data, **self._options)

    def load(self, data, **options):
        """Load the widget with data. If running in client mode, this method
        serializes the data and calls the browser viewer's load method.
        Otherwise, it calls `Viewer.load()` using `super()`.
        """
        if self.client is True:
            # serialize the data and send a custom message to the browser
            if isinstance(data, pandas.DataFrame) or isinstance(data, pandas.Series):
                data, _ = deconstruct_pandas(data)
            d = _serialize(data)
            self._data = d
        else:
            # Viewer will ignore **options if `data` is a Table or View.
            super(PerspectiveWidget, self).load(data, **options)

            # Do not enable editing if the table is unindexed.
            if self.editable and self.table._index == "":
                logging.critical("Cannot edit on an unindexed `perspective.Table`!")
                self.editable = False

        # Notify front-end of load immediately.
        message = self._make_load_message()
        self.send(message.to_dict())

    def update(self, data):
        """Update the widget with new data. If running in client mode, this
        method serializes the data and calls the browser viewer's update
        method. Otherwise, it calls `Viewer.update()` using `super()`.
        """
        if self.client is True:
            if self._displayed is False:
                self._predisplay_update_cache.append(data)
                return

            # serialize the data and send a custom message to the browser
            if isinstance(data, pandas.DataFrame) or isinstance(data, pandas.Series):
                data, _ = deconstruct_pandas(data)
            d = _serialize(data)
            self.post({"cmd": "update", "data": d})
        else:
            super(PerspectiveWidget, self).update(data)

    def clear(self):
        """Clears the widget's underlying `Table`.

        In client mode, clears the `_data` attribute of the widget.
        """
        if self.client is True:
            self.post({"cmd": "clear"})
            self._data = None
        else:
            super(PerspectiveWidget, self).clear()

    def replace(self, data):
        """Replaces the widget's `Table` with new data conforming to the same
        schema. Does not clear user-set state. If in client mode, serializes
        the data and sends it to the browser.
        """
        if self.client is True:
            if isinstance(data, pandas.DataFrame) or isinstance(data, pandas.Series):
                data, _ = deconstruct_pandas(data)
            d = _serialize(data)
            self.post({"cmd": "replace", "data": d})
            self._data = d
        else:
            super(PerspectiveWidget, self).replace(data)

    def delete(self, delete_table=True):
        """Delete the Widget's data and clears its internal state. If running in
        client mode, sends the `delete()` command to the browser. Otherwise
        calls `delete` on the underlying viewer.

        Args:
            delete_table (`bool`): whether the underlying `Table` will be
                deleted. Defaults to True.
        """
        if self.client is False:
            super(PerspectiveWidget, self).delete(delete_table)
        self.post({"cmd": "delete"})

        # Close the underlying comm and remove widget from the front-end
        self.close()

    def post(self, msg, msg_id=None, binary=False):
        """Post a serialized message to the `PerspectiveJupyterClient`
        in the front end.

        The posted message should conform to the `PerspectiveJupyterMessage`
        interface as defined in `@finos/perspective-jupyterlab`.

        Args:
            msg (dict): a message from `PerspectiveManager` for the front-end
                viewer to process.
            msg_id (int): an integer id that allows the client to process
                the message.
            binary (bool): whether the message contains binary buffers that
                should be sent with a special protocol.
        """
        if binary:
            # The front end will read `buffers` properly.
            self.send(None, buffers=[msg])
        else:
            message = _PerspectiveWidgetMessage(msg_id, "cmd", msg)
            self.send(message.to_dict())

    @observe("value")
    def handle_message(self, widget, content, buffers):
        """Given a message from `PerspectiveJupyterClient.send()`, process the
        message and return the result to `self.post`.

        Args:
            widget: a reference to the `Widget` instance that received the
                message.
            content (dict): the message from the front-end. Automatically
                de-serialized by ipywidgets.
            buffers : optional arraybuffers from the front-end, if any.
        """
        if self._pending_binary:
            msg = self._pending_binary

            # arrow is a `MemoryView` - convert to bytes
            arrow = buffers[0].tobytes()
            msg["args"].insert(0, arrow)

            # Send the message to the manager to process
            post_callback = partial(self.post, msg_id=msg["id"])
            self.manager._process(msg, post_callback)
            self._pending_binary = None
            return

        if content["type"] == "cmd":
            parsed = json.loads(content["data"])

            if parsed["cmd"] == "init":
                self.post({"id": -1, "data": None})
            elif parsed["cmd"] == "table":
                # return the dataset or table name to the front-end
                msg = self._make_load_message()
                self.send(msg.to_dict())

                # In client mode, users can call `update()` before the widget
                # is visible. This applies the updates after the viewer has
                # loaded the initial dataset.
                if self.client is True and len(self._predisplay_update_cache) > 0:
                    for data in self._predisplay_update_cache:
                        self.update(data)
            else:
                # If the message has `binary_length` set, wait for the arrow
                # and join it with the JSON message.
                if parsed.get("binary_length"):
                    self._pending_binary = parsed
                    return

                # For all calls to Perspective, process it in the manager.
                post_callback = partial(self.post, msg_id=parsed["id"])
                self.manager._process(parsed, post_callback)

    def _make_load_message(self, index=None, limit=None):
        """Send a message to the front-end either containing the name of a
        hosted view in Python, so the front-end can create a table in the
        Perspective WebAssembly client, or if `server` is True, the name of a
        Table in python, or the serialized dataset with options if `client`
        is True.

        If the front-end requests data and it has not been loaded yet,
        an error will be logged, and the front-end will wait for `load()` to
        be called, which will notify the front-end of new data.
        """
        msg_data = None

        if self.client and self._data is not None:
            # Send serialized data to the browser, which will run Perspective
            # in client mode: there is no table in the Python kernel.
            msg_data = {"data": self._data, "options": self._options}
        elif self.server and self.table_name is not None:
            # If the `server` kwarg is set during initialization, Perspective
            # will run in server-only mode, where a Table is hosted in the
            # kernel and the front-end proxies pivots, sorts, data requests
            # etc. to the kernel and does not run a Table in the front-end.
            msg_data = {"table_name": self.table_name}
        elif self._perspective_view_name is not None:
            # If a view is hosted by the widget's manager (by default),
            # run Perspective in client-server mode: a Table will be created
            # in the front-end that mirrors the Table hosted in the kernel,
            # and updates and edits will be synchronized across the client
            # and the server.
            msg_data = {
                "table_name": self.table_name,
                "view_name": self._perspective_view_name,
                "options": {},
            }

            if self.table._index is not None:
                msg_data["options"]["index"] = self.table._index
            elif self.table._limit is not None:
                msg_data["options"]["limit"] = self.table._limit

        if msg_data is not None:
            return _PerspectiveWidgetMessage(-2, "table", msg_data)
        else:
            raise PerspectiveError(
                "Widget does not have any data loaded - use the `load()` method to provide it with data."
            )

    def _on_display(self, widget, **kwargs):
        """When the widget has been displayed, make sure `displayed` is set to
        True so updates stop being cached.
        """
        self._displayed = True
