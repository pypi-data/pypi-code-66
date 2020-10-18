# coding="utf-8"

import requests
import json
import configparser
import time


class wechatntf():

    def __init__(self):
        self.url = "http://wxpusher.zjiecode.com/api/send/message"
        self.headers = {
            "Content-Type": "application/json"
        }
        self.config = configparser.ConfigParser()

    def wechatsend(self, summary="", content="", contentType=1):

        """
        主体方法
        :param summary: 通知概览
        :param content: 通知内容
        :param contentType: 通知类型，1-文字，2-html(只发送body标签内部的数据即可，不包括body标签)，3-markdown
        :return: 请求结果，成功会有json格式的结果
        """
        self.data = {
            "summary": summary,
            "content": content,
            "contentType": contentType
        }
        self.config.read('./config/wechatntf_config.cfg')  # 读取配置文件信息

        self.data["appToken"] = self.config.get('DEFAULT', 'appToken')
        # 配置文件获取到的[424] 为str形式，转换为python数据格式，需loads
        self.data["topicIds"] = json.loads(self.config.get('DEFAULT', 'topicIds'))
        self.data = json.dumps(self.data)
        i = 0
        # 如果数据发送超时，则进行5次发送尝试
        while i < 5:
            try:
                res = requests.post(url=self.url, headers=self.headers, data=self.data,
                              timeout=3).content.decode()

                return res
            except Exception as ret:
                time.sleep(0.5)
                i += 1


if __name__ == '__main__':
    a = wechatntf()
    res = a.wechatsend(content="这是一条测试消息")
    print(res)
