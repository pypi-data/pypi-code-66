from typing import (
    Callable,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    import datawelder.readwrite

import datawelder.partition


def extract(
    reader: 'datawelder.readwrite.AbstractReader',
    writer: 'datawelder.readwrite.AbstractWriter',
    total_partitions: int,
    partition_num: int,
    key_index: int = 0,
    key_function: Callable[[str, int], int] = datawelder.partition.calculate_key,
) -> None:
    for i, record in enumerate(reader, 1):
        key = record[key_index]
        partition_index = key_function(key, total_partitions)
        if partition_index == partition_num:
            writer.write(record)
