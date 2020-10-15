"""Dicom metadata module"""
import logging
from copy import copy

import pydicom
from pydicom.dataelem import RawDataElement

from flywheel_metadata.file.dicom.fixer import fw_pydicom_config

log = logging.getLogger(__name__)


def load_dicom(*args, decode=True, config=None, tracker=None, **kwargs):
    """
    Load and optionally decode Dicom dataset with Flywheel pydicom configuration.

    Args:
        *args: pydicom.dcmread args.
        decode (bool): decode the dataset if True (default=True).
        config (dict): the kwargs to be passed to the fw_pydicom_config manager (default=None).
        tracker (Tracker): A Tracker instance (default=None).
        **kwargs: pydicom.dcmread kwargs.

    Returns:
        pydicom.Dataset: a pydicom Dataset.
    """
    if not config:
        config = {}

    # Getting the encoding
    # Currently needed by the backslash_in_VM1_string_callback
    # TODO: revise once https://github.com/pydicom/pydicom/pull/1218 is merged
    try:
        dcm = pydicom.dcmread(*args, **kwargs, specific_tags=[])
    # Handle DicomDirs which will except if DirectoryRecordSequence is not defined
    except AttributeError:
        dcm = pydicom.dcmread(
            *args, **kwargs, specific_tags=["DirectoryRecordSequence"]
        )
    encoding = dcm.read_encoding or dcm._character_set

    with fw_pydicom_config(tracker=tracker, encoding=encoding, **config):
        dicom_ds = pydicom.dcmread(*args, **kwargs)
        if decode:
            dicom_ds.decode()

    return dicom_ds
