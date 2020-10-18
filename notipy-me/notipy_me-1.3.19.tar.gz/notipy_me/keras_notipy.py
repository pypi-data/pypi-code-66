from typing import Dict
from tensorflow.keras.callbacks import Callback
from sanitize_ml_labels import sanitize_ml_labels
from .notipy_me import Notipy


class KerasNotipy(Callback):

    def __init__(
        self,
        task_name: str = None,
        metadata: Dict = None,
        report_only_validation: bool = True,
        sanitize_metrics: bool = True
    ):
        """Create new Keras Notipy object.

        Parameters
        -----------------
        task_name: str = None,
            Optional name of the task to use for report.
        metadata: Dict = None,
            Optional metadata to be reported alongside data.
        report_only_validation: bool = True,
            Report only metrics relative to the validation set.
        sanitize_metrics: bool = True,
            Sanitize the names of the metrics.
        """
        super().__init__()
        self._metadata = {} if metadata is None else metadata
        self._notipy = Notipy(task_name=task_name)
        self._report_only_validation = report_only_validation
        self._sanitize_metrics = sanitize_metrics

    def on_train_begin(self, logs=None):
        """Start notipy as the training begins."""
        self._notipy.enter()

    def on_epoch_end(self, epoch: int, logs=None):
        """When the epoch ends we report how the model is doing."""
        if logs is not None:
            self._notipy.add_report({
                **self._metadata,
                **{
                    sanitize_ml_labels(metric) if self._sanitize_metrics else metric : value
                    for metric, value in logs.items()
                    if not self._report_only_validation and metric.startswith("val")
                },
                "epoch": epoch
            })

    def on_train_end(self, logs=None):
        """When the training is complete we close down also the Notipy."""
        self._notipy.exit()
