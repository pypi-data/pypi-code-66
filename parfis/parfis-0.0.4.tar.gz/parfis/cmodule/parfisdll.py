import os
import numpy as np
from ctypes import cdll, c_char_p

class Parfis:
    log_fname = "parfis.log"

    def __init__(self, ptr: c_char_p):
        self.ptr = ptr
        ParfisAPI.set_log_file(Parfis.log_fname)

    @staticmethod
    def set_log_file(fname: str):
        Parfis.log_fname = fname
        

    # def __del__(self):
    #     self.delete()

    # def delete(self):
    #     return ParfisAPI.deleteParfis(self)

    # def add_part(self, data: str):
    #     return SnnAPI.add_part(self, data)

    # def get_params(self, pid: int) -> str:
    #     return SnnAPI.get_params(self, pid)

    # def get_vo(self, pid: int) -> float:
    #     return SnnAPI.get_vo(self, pid)

    # def get_vi(self, pid: int) -> float:
    #     return SnnAPI.get_vi(self, pid)

    # def get_param(self, pid: int, data: str) -> float:
    #     return SnnAPI.get_param(self, pid, data)

    # def set_params(self, pid: int, data: str):
    #     return SnnAPI.set_params(self, pid, data)

    # def set_params_dbarr(self, pid: int, key: str, data):
    #     data_ptr = POINTER(c_double)((c_double * len(data))(*data))
    #     return SnnAPI.set_params_dbarr(self, pid, key, data_ptr)

    # def set_recorder(self, data: str):
    #     return SnnAPI.set_recorder(self, data)

    # def save_net(self, filename: str):
    #     return SnnAPI.save_net(self, filename)

    # def load_net(self, filename: str):
    #     return SnnAPI.load_net(self, filename)

    # def reset(self):
    #     return SnnAPI.reset_net(self)

    # def run(self, steps: int, dt: float):
    #     return SnnAPI.run_net(self, steps, dt)

    # def get_record(self, rid: int) -> Record:
    #     data_ptr = POINTER(c_double)()
    #     pc_ptr = POINTER(c_uint32)()
    #     size = SnnAPI.get_recorder_ptr(self, rid, data_ptr, pc_ptr)
    #     return Record(size, data_ptr, pc_ptr)

    # def connect_syna(self):
    #     return SnnAPI.connect_syna(self)


class ParfisAPI:
    path = os.path.join(os.path.dirname(__file__), "lib\\parfis.dll")
    api = cdll.LoadLibrary(path)
    api.ParfisAPI_setLogFile.argtypes = [c_char_p]

    @staticmethod
    def set_log_file(fname: str):
        return ParfisAPI.api.ParfisAPI_setLogFile(fname.encode())

    # api.SnnAPI_deleteNet.argtypes = [c_void_p]
    # api.SnnAPI_newNet.restype = c_void_p
    # api.SnnAPI_getLog.restype = c_char_p
    # api.SnnAPI_addPart.argtypes = [c_void_p, c_char_p]
    # api.SnnAPI_getParams.argtypes = [c_void_p, c_uint32]
    # api.SnnAPI_getParams.restype = c_char_p
    # api.SnnAPI_setParams.argtypes = [c_void_p, c_uint32, c_char_p]
    # api.SnnAPI_setParamsDBArray.argtypes = [c_void_p, c_uint32, c_char_p,
    #                                         POINTER(POINTER(c_double))]
    # api.SnnAPI_setRecorder.argtypes = [c_void_p, c_char_p]
    # api.SnnAPI_setRecorder.restype = c_uint32
    # api.SnnAPI_resetNet.argtypes = [c_void_p]
    # api.SnnAPI_runNet.argtypes = [c_void_p, c_uint32, c_double]
    # api.SnnAPI_saveNet.argtypes = [c_void_p, c_char_p]
    # api.SnnAPI_loadNet.argtypes = [c_void_p, c_char_p]
    # api.SnnAPI_getRecorderPtr.argtypes = [c_void_p, c_uint32, POINTER(POINTER(c_double)),
    #                                       POINTER(POINTER(c_uint32))]
    # api.SnnAPI_getRecorderPtr.restype = c_uint32
    # api.SnnAPI_connectSyna.argtypes = [c_void_p]
    # api.SnnAPI_connectSyna.restype = c_uint32
    # api.SnnAPI_getParam.argtypes = [c_void_p, c_uint32, c_char_p]
    # api.SnnAPI_getParam.restype = c_double
    # api.SnnAPI_getVi.argtypes = [c_void_p, c_uint32]
    # api.SnnAPI_getVi.restype = c_double
    # api.SnnAPI_getVo.argtypes = [c_void_p, c_uint32]
    # api.SnnAPI_getVo.restype = c_double

    # @staticmethod
    # def new_net() -> Net:
    #     return Net(SnnAPI.api.SnnAPI_newNet())

    # @staticmethod
    # def clear_log():
    #     SnnAPI.api.SnnAPI_clearLog()

    # @staticmethod
    # def get_log() -> str:
    #     return SnnAPI.api.SnnAPI_getLog().decode("utf-8")

    # @staticmethod
    # def delete_net(net: Net):
    #     SnnAPI.api.SnnAPI_deleteNet(net.ptr)
    #     net.ptr = None

    # @staticmethod
    # def add_part(net: Net, data: str):
    #     SnnAPI.api.SnnAPI_addPart(net.ptr, data.encode())

    # @staticmethod
    # def get_params(net: Net, pid: int) -> str:
    #     return SnnAPI.api.SnnAPI_getParams(net.ptr, pid).decode("utf-8")

    # @staticmethod
    # def get_vo(net: Net, pid: int) -> float:
    #     return SnnAPI.api.SnnAPI_getVo(net.ptr, pid)

    # @staticmethod
    # def get_vi(net: Net, pid: int) -> float:
    #     return SnnAPI.api.SnnAPI_getVi(net.ptr, pid)

    # @staticmethod
    # def get_param(net: Net, pid: int, data: str) -> float:
    #     return SnnAPI.api.SnnAPI_getParam(net.ptr, pid, data.encode())

    # @staticmethod
    # def set_params(net: Net, pid: int, data: str) -> None:
    #     return SnnAPI.api.SnnAPI_setParams(net.ptr, pid, data.encode())

    # @staticmethod
    # def set_params_dbarr(net: Net, pid: int, key: str, data_ptr) -> None:
    #     return SnnAPI.api.SnnAPI_setParamsDBArray(net.ptr, pid, key.encode(), byref(data_ptr))

    # @staticmethod
    # def set_recorder(net: Net, data: str) -> int:
    #     return SnnAPI.api.SnnAPI_setRecorder(net.ptr, data.encode())

    # @staticmethod
    # def reset_net(net: Net):
    #     return SnnAPI.api.SnnAPI_resetNet(net.ptr)

    # @staticmethod
    # def run_net(net: Net, steps: int, dt: float):
    #     return SnnAPI.api.SnnAPI_runNet(net.ptr, steps, dt)

    # @staticmethod
    # def save_net(net: Net, filename: str):
    #     return SnnAPI.api.SnnAPI_saveNet(net.ptr, filename.encode())

    # @staticmethod
    # def load_net(net: Net, filename: str):
    #     return SnnAPI.api.SnnAPI_loadNet(net.ptr, filename.encode())

    # @staticmethod
    # def get_recorder_ptr(net: Net, rid: int, data_ptr, pc_ptr) -> int:
    #     return SnnAPI.api.SnnAPI_getRecorderPtr(net.ptr, rid, byref(data_ptr), byref(pc_ptr))

    # @staticmethod
    # def print_log_file():
    #     return SnnAPI.api.SnnAPI_printLogFile()

    # @staticmethod
    # def connect_syna(net: Net):
    #     return SnnAPI.api.SnnAPI_connectSyna(net.ptr)
