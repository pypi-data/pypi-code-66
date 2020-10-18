import brotli
from typing import Union, Tuple, Optional, Generator
from .utils import process_varint, process_varstr


def read_footer(data: bytes) -> Tuple[bytes, bytes]:
    footer_len = int.from_bytes(data[-4:], 'little', signed=False)
    data = data[:-4]
    body, footer = data[:-footer_len], data[-footer_len:]
    return body, footer


def read_store(body: bytes) -> Tuple[bytes, bytes, int]:
    offset = int.from_bytes(body[-12:-4], 'little', signed=False)
    max_doc = int.from_bytes(body[-4:], 'little', signed=False)
    return body[:offset], body[offset:-12], max_doc


def parse_footer(footer: bytes) -> Tuple[int, int, bytes]:
    footer_length, length = process_varint(footer)
    footer = footer[length:]
    version = int.from_bytes(footer[:4], 'little', signed=False)
    crc = int.from_bytes(footer[4:8], 'little', signed=False)
    compression, _ = process_varstr(footer[8:])
    return version, crc, compression


class TantivyReader:
    def __init__(self, store: bytes, schema: dict):
        self.store = store
        self.schema = schema

    def _decode_document(self, reader: bytes) -> dict:
        num_field_values, length = process_varint(reader)
        reader = reader[length:]
        document = {}
        for _ in range(num_field_values):
            field_id, value, reader = self._decode_field(reader)
            if self.schema[field_id]['name'] not in document:
                document[self.schema[field_id]['name']] = []
            document[self.schema[field_id]['name']].append(value)
        return document

    def _decode_field(self, reader: bytes) -> Tuple[int, Union[Optional[bytes], int], bytes]:
        field_id = int.from_bytes(reader[:4], 'little', signed=False)
        type_ = int.from_bytes(reader[4:5], 'little', signed=False)
        reader = reader[5:]
        if type_ == 0:
            value, length = process_varstr(reader)
            value = value.decode()
            reader = reader[length:]
        elif type_ == 1:
            value = int.from_bytes(reader[:8], 'little', signed=False)
            reader = reader[8:]
        elif type_ == 2:
            value = int.from_bytes(reader[:8], 'little', signed=True)
            reader = reader[8:]
        else:
            return field_id, None, reader
        return field_id, value, reader

    def documents(self) -> Generator[dict]:
        """
        Iterates over all document inside `.store`

        Returns:
            Document generator
        """
        body, footer = read_footer(self.store)
        store, skip_list, max_doc = read_store(body)
        while store:
            block_size = int.from_bytes(store[:4], 'little', signed=False)
            decompressed = brotli.decompress(store[4:block_size + 4])
            while decompressed:
                doc_length, length = process_varint(decompressed)
                decompressed = decompressed[length:]
                document = self._decode_document(decompressed)
                yield document
                decompressed = decompressed[doc_length:]
            store = store[block_size + 4:]

