from typing import Union, Optional

List_or_Int = Union[int, list]
Tuple_or_Int = Union[tuple, int]

class LightningConfig:
    def __init__(self, gpus: Optional[Tuple_or_Int]=None, epoches: Optional[Tuple_or_Int]=None) -> None:
        self._gpus = gpus
        self._epoches = epoches

    @property
    def gpus(self):
        return self._gpus

    @property
    def max_epoch(self) -> int:
        if isinstance(self._epoches, int):
            return self._epoches
        elif isinstance(self._epoches, tuple):
            return self._epoches[-1]
        else:
            return 1

    @property
    def min_epoch(self) -> int:
        if isinstance(self._epoches, int):
            return self._epoches
        elif isinstance(self._epoches, tuple):
            return self._epoches[0]
        else:
            return 1