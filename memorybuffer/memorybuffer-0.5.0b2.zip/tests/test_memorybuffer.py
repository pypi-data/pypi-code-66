# Copyright (c) 2012-2020 Adam Karpierz
# Licensed under the zlib/libpng License
# https://opensource.org/licenses/Zlib

import unittest
import array
import ctypes as ct

from memorybuffer import Py_buffer, Buffer, isbuffer


class BufferBase(Buffer):

    # Buffer protocol

    def __getbuffer__(self, buffer: Py_buffer, flags: int):
#        print("__getbuffer__", self.__buffer_exports__, type(flags), flags, Py_buffer.PyBUF_FULL_RO, buffer.len, buffer.itemsize, buffer.ndim, type(buffer.obj))
        length   = len(self.byte_buffer)
        itemsize = 1
        buffsize = length * itemsize

        buffer.buf        = self.__from_buffer__(self.byte_buffer, buffsize)
        buffer.len        = buffsize
        buffer.itemsize   = itemsize
        buffer.readonly   = self.readonly
        buffer.ndim       = 1
        buffer.format     = b"b"
        buffer.shape      = (ct.c_ssize_t * buffer.ndim)(length)
        buffer.strides    = (ct.c_ssize_t * buffer.ndim)(itemsize)
        buffer.suboffsets = None
        buffer.internal   = None

    def __releasebuffer__(self, buffer: Py_buffer):
#        print("__releasebuffer__", self.__buffer_exports__)
        if self.__buffer_exports__ == 0 and buffer.buf:
            buffer.buf = None


class BytearrayBuffer(BufferBase):

    def __init__(self):
        # self.byte_buffer, self.readonly = ct.create_string_buffer(b"ABCDEFGHIJ"), True
        self.byte_buffer, self.readonly = bytearray(b"ABCDEFGHIJ"), False


class ArrayByteBuffer(BufferBase):

    def __init__(self):
        self.byte_buffer, self.readonly = array.array("B", b"ABCDEFGHIJ"), False


class CtypesByteBuffer(BufferBase):

    def __init__(self):
        self.byte_buffer, self.readonly = (ct.c_ubyte * 10)(*list(b"ABCDEFGHIJ")), False


class MemoryBufferTestCase(unittest.TestCase):

    def test_simple_byte_buffer(self):

        no_buf = 123
        self.assertFalse(isbuffer(no_buf))

        for ByteBuffer in (BytearrayBuffer, ArrayByteBuffer, CtypesByteBuffer):

            buf = ByteBuffer()
            self.assertTrue(isbuffer(buf))

            mem = memoryview(buf)

            self.assertSequenceEqual(bytes(mem), b"ABCDEFGHIJ")
            self.assertSequenceEqual(bytearray(mem), bytearray(b"ABCDEFGHIJ"))
            self.assertSequenceEqual(tuple(mem), tuple(b"ABCDEFGHIJ"))
            self.assertSequenceEqual(list(mem), list(b"ABCDEFGHIJ"))

            mem[0] = ord("X")
            mem[5] = ord("Z")
            self.assertSequenceEqual(bytes(mem), b"XBCDEZGHIJ")
            self.assertSequenceEqual(bytearray(mem), bytearray(b"XBCDEZGHIJ"))
            self.assertSequenceEqual(tuple(mem), tuple(b"XBCDEZGHIJ"))
            self.assertSequenceEqual(list(mem), list(b"XBCDEZGHIJ"))
