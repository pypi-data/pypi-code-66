# _*_ coding:utf-8 _*_
import base64
import hashlib
import time
import requests
import logging

from wiz_utils.string_utils import StringUtils

import hmac

from src.wiz_dingtalk.message import Message


class DingTalkBot(object):
    base_url = "https://oapi.dingtalk.com/robot/send"

    def __init__(self, token: str, secret: str = None):
        self._secret = secret
        self._token = token

    @property
    def secret(self):
        return self._secret

    @property
    def token(self):
        return self._token

    def send(self, message: Message = None, json_message: str = None):
        ts = int(time.time() * 1000)
        params = {"access_token": self.token, "timestamp": ts}
        if StringUtils.is_not_blank(self.secret):
            string_to_sign = "%s\n%s" % (ts, self.secret)
            sign = base64.b64encode(hmac.new(self.secret.encode("utf-8"), string_to_sign.encode("utf-8"),
                                             digestmod=hashlib.sha256).digest())
            params['sign'] = sign
        try:
            request_body = message.to_json() if message is not None else json_message
            if StringUtils.is_blank(request_body):
                raise AttributeError("request body is null")
            response = requests.post(url=self.base_url, params=params,
                                     headers={"Content-Type": "application/json; charset=utf-8"}, data=request_body)
            print(response.content)
        except Exception as e:
            logging.error("send message error", e)
