import hashlib
import secrets
import time

__all__ = ["DtkBase"]


class DtkBase(object):
    """
    大淘客基础请求类
    """

    def __init__(self, app_key: str, app_secret: str):
        self._app_key = app_key
        self._app_secret = app_secret

    @property
    def app_key(self) -> str:
        return self._app_key

    @property
    def app_secret(self) -> str:
        return self._app_secret

    def merge_args(self, d: dict, version: str) -> dict:
        d["appKey"] = self._app_key
        d["version"] = version

        # https://www.dataoke.com/pmc/open-gz.html?id=41
        nonce = secrets.token_urlsafe(6)
        timer = int(time.time() * 1000)
        key = self._app_secret
        d["nonce"] = nonce
        d["timer"] = timer
        s = f"appKey={self._app_key}&timer={timer}&nonce={nonce}&key={key}"
        h = hashlib.md5(s.encode())
        d["signRn"] = h.hexdigest().upper()
        return d
