import threading
import psutil
import asyncio
from nutellaAgent import nutellaRequests

class Nutella(threading.Thread):

    def __init__(self):
        self.requestData=dict()
        self.modelName=""
        self.projectKey=""
        self.stepNumber=0
        self.indicatorData=dict()
        self.psValue=psutil.Process()
        self.requestUrl="http://localhost:7000/admin/sdk"


    def init(self,modelName=None, projectKey=None, reinit=False):
        self.projectKey=projectKey
        self.modelName =modelName
        self.requestData["reinit"] = reinit # 일단 제외.
        requestDatas = nutellaRequests.Requests()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(requestDatas.requestAction(requestDatas=self.indicatorDatas, url=self.requestUrl))
        loop.close()

    def config(self,**configDatas): # 이것도 제외.
        for key,value in configDatas.items():
            self.requestData[key]=value

    def log(self,**indicatorDatas):
        self.indicatorData["modeName"]=self.modelName
        for key,value in indicatorDatas.items():
            self.indicatorData[key]=value
        requestDatas = nutellaRequests.Requests()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(requestDatas.requestAction(requestDatas=self.indicatorDatas, url=self.requestUrl))
        loop.close()

    def hardwareSystemValue(self):
        p = psutil.Process()
        self.requestData["cpu"]=min(65535, int(((p.cpu_percent(interval=None) / 100) / psutil.cpu_count(False)) * 65535))
        self.requestData["memory"]= min(65535, int((p.memory_percent() / 100) * 65535))
        self.requestData["net"]=psutil.net_io_counters()
        self.requestData["disk"]=psutil.disk_io_counters()

    def setRequestUrl(self,url):
        self.requestUrl=url