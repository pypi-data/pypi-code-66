from typing import Dict
from tensorflow.keras.callbacks import Callback
from .notipy_me import Notipy


class KerasNotipy(Callback):

    def __init__(self, task_name: str = None, metadata: Dict = None):
        """Create new Keras Notipy object.

        Parameters
        -----------------
        task_name: str = None,
            Optional name of the task to use for report.
        metadata: Dict = None,
            Optional metadata to be reported alongside data.
        """
        super().__init__()
        self._metadata = {} if metadata is None else metadata
        self._notipy = Notipy(task_name)

    def on_train_begin(self, logs=None):
        """Start notipy as the training begins."""
        self._notipy.enter()

    def on_epoch_end(self, epoch: int, logs=None):
        """When the epoch ends we report how the model is doing."""
        if logs is not None:
            self._notipy.add_report({
                **self._metadata,
                **logs,
                "epoch": epoch
            })

    def on_train_end(self, logs=None):
        """When the training is complete we close down also the Notipy."""
        self._notipy.exit()
