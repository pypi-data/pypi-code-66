#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import requests
from requests.adapters import HTTPAdapter

import sys
import time
import hashlib


def randomIP():
    a = random.sample(list(range(1, 256)) * 4, 4)
    b = map(str, a)
    ip = '.'.join(b)
    return ip


class RabbitHttp:
    def __init__(self, timeout=5, post_headers={}, get_headers={}, fake_ip=True, ):
        """
        :param timeout: : 每个请求的超时时间
        :param post_headers: POST协议头
        :param get_headers: GET协议头
        :param fake_ip: 是否开启随机ip
        """
        self.get_headers = get_headers
        self.post_headers = post_headers
        s = requests.Session()
        #: 在session实例上挂载Adapter实例, 目的: 请求异常时,自动重试
        s.mount('http://', HTTPAdapter(max_retries=3))
        s.mount('https://', HTTPAdapter(max_retries=3))

        #: 设置为False, 主要是HTTPS时会报错, 为了安全也可以设置为True
        s.verify = False

        #: 公共的请求头设置
        fakeHeaders = {"X-Forwarded-For": randomIP() + ',' + randomIP() + ',' + randomIP(), "X-Forwarded": randomIP(),
                       "Forwarded-For": randomIP(), "Forwarded": randomIP(),
                       "X-Forwarded-Host": randomIP(), "X-remote-IP": randomIP(),
                       "X-remote-addr": randomIP(), "True-Client-IP": randomIP(),
                       "X-Client-IP": randomIP(), "Client-IP": randomIP(), "X-Real-IP": randomIP(),
                       "Ali-CDN-Real-IP": randomIP(), "Cdn-Src-Ip": randomIP(), "Cdn-Real-Ip": randomIP(),
                       "X-Cluster-Client-IP": randomIP(),
                       "WL-Proxy-Client-IP": randomIP(), "Proxy-Client-IP": randomIP(),
                       "Fastly-Client-Ip": randomIP(), "True-Client-Ip": randomIP()
                       }
        if fake_ip:
            post_headers.update(fakeHeaders)
            get_headers.update(fakeHeaders)

        #: 挂载到self上面
        self.s = s
        self.s.timeout = timeout

    def get(self, url):
        """GET

        :param url:
        :param query_dict: 一般GET的参数都是放在URL查询参数里面
        :return:
        """
        print('GET==>' + url)
        return self.s.get(url, headers=self.get_headers)

    def post(self, url, form_data=None, body_dict=None):
        """POST

        :param url:
        :param form_data: 有时候POST的参数是放在表单参数中
        :param body_dict: 有时候POST的参数是放在请求体中(这时候 Content-Type: application/json )
        :return:
        """
        if form_data:
            print('POST==>' + url)
            print('DATA==>', str(form_data))
            return self.s.post(url, data=form_data, headers=self.post_headers)
        if body_dict:
            print('POST==>' + url)
            print('JSON==>', str(body_dict))
            return self.s.post(url, json=body_dict, headers=self.post_headers)

    def get_proxy_ip(self):
        url = 'http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=1246e578e8b25ba691cae4a0688fdc4d&orderNo=GL20200920152845GpOaPZCY&count=1&isTxt=1&proxyType=1'

    def __del__(self):
        """当实例被销毁时,释放掉session所持有的连接

        :return:
        """
        if self.s:
            self.s.close()


# DT20201016142903kYRBHjby
# 6f42c70cda3c84de9f9b66f41a078f06
class Proxy(object):
    # 新用户只需要替换14行和15行的orderno和secret即可运行

    _version = sys.version_info
    is_python3 = (_version[0] == 3)

    def __init__(self, orderno, secret, type=1, https=False):
        # 个人中心获取orderno与secret
        self.orderno = orderno
        self.secret = secret
        self.ip = "dynamic.xiongmaodaili.com"
        if type == 0:
            # 按量订单端口
            self.port = "8088"
        if type == 1:
            # 按并发订单端口
            self.port = "8089"
        self.https = https
        ip_port = self.ip + ":" + self.port
        if self.https:
            # https协议的网站用此配置
            self.proxy = {"https": "https://" + ip_port}
        else:
            # http协议的网站用此配置
            self.proxy = {"http": "http://" + ip_port}

    def get_auth_header_and_proxy(self):

        timestamp = str(int(time.time()))  # 计算时间戳
        txt = "orderno=" + self.orderno + "," + "secret=" + self.secret + "," + "timestamp=" + timestamp

        if self.is_python3:
            txt = txt.encode()

        md5_string = hashlib.md5(txt).hexdigest()  # 计算sign
        sign = md5_string.upper()  # 转换成大写
        print(sign)
        auth = "sign=" + sign + "&" + "orderno=" + self.orderno + "&" + "timestamp=" + timestamp + "&change=true"

        print(auth)

        print(proxy)
        headers = {"Proxy-Authorization": auth}
        return headers, self.proxy


if __name__ == '__main__':
    proxy = Proxy('DT20201016142903kYRBHjby', '6f42c70cda3c84de9f9b66f41a078f06')
    print(proxy.get_auth_header_and_proxy()[0])
    print(proxy.get_auth_header_and_proxy()[1])
