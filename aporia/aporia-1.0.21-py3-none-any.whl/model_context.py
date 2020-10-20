from typing import Dict, Optional

from aporia.api.types import FeatureValue


class ModelContext:
    """Context object for prediction syntax sugar."""

    __slots__ = ["extra_inputs", "extra_outputs"]

    def __init__(
        self,
        extra_inputs: Optional[Dict[str, FeatureValue]] = None,
        extra_outputs: Optional[Dict[str, FeatureValue]] = None,
    ):
        """Initializes a ModelContext object.

        Args:
            extra_inputs (Dict[str, FeatureValue], optional): Extra inputs. Defaults to None.
            extra_outputs (Dict[str, FeatureValue], optional): Extra outputs. Defaults to None.
        """
        self.extra_inputs = extra_inputs
        self.extra_outputs = extra_outputs
