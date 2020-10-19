import hashlib
import base64
from _pysha3 import keccak_256
from ecdsa import SigningKey, SECP256k1

def ecdsa_verifing(signature, data, verifing_key, hashfunc=hashlib.sha256):
    """
    AOS ECDSA 验证签名
    :param verifing_key:
    :param signature:
    :param data:
    :param hashfunc:
    :return:
    """
    verify = verifing_key.verify(signature=signature, data=data, hashfunc=hashfunc)
    return verify

def ecdsa_sign(data, privkey, hashfunc=hashlib.sha256):
    """
    AOS ECDSA 签名
    :param data:
    :param privkey:
    :param hashfunc:
    :return:
    """
    if len(privkey) == 66:
        privkey = privkey[2:]
    elif privkey != 64:
        return 0, 0, 0
    signning_key = SigningKey.from_string(bytes.fromhex(privkey), curve=SECP256k1)
    verifing_key = signning_key.get_verifying_key()
    signature = signning_key.sign(data, hashfunc=hashfunc)
    return signature, data, verifing_key

def base64_decode(base_data):
    """
    AOS Base64解密
    :param base_data:
    :return:
    """
    bytes_data = base64.b64decode(base_data)
    return bytes_data

def base64_encode(bytes_data):
    """
    AOS Base64加密
    :param bytes_data:
    :return:
    """
    base_data = base64.b64encode(bytes_data)
    return bytes.decode(base_data)

def Hash(msg):
    """
    AOS Hash加密
    :return:
    """
    if isinstance(msg, str):
        msg = bytes(msg, encoding="utf8")
    k = keccak_256()
    k.update(msg)
    return k.hexdigest()

def binary_to_list(bin):
    list = []
    for idx, val in enumerate(bin):
        list.append(val)
    return list


def list_to_binary(list):
    bin = b''
    for i in list:
        bin += bytes([i])
    return bin
a = Hash(b'hello')
print(a)