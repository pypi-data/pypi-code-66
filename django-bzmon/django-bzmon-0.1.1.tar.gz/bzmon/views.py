from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from loguru import logger
import psutil

# Create your views here.
def bzmon(request):
    config = settings.BZMON_CONFIG
    logger.info(config)
    if config["token"]["required"]:
        token = request.GET.get('token')
        if not token or token != config["token"]["token"]:
            return HttpResponse('Unauthorized', status=401)
    results = {
        "contacts": config["contacts"] if config["contacts"] else [],
        "memory": {},
        "storage": []
    }
    if config["monitor"]["memory"]:
        memory_usage = psutil.virtual_memory()
        results["memory"] = {
            "total": memory_usage.total,
            "available": memory_usage.available,
            "used": memory_usage.used,
            "free": memory_usage.free,
            "percent": memory_usage.percent,"warn": config["memory"]["warn"],
            "warn_level": config["memory"]["warn_level"]
        }
    if config["monitor"]["storage"]:
        for path in config["storage"]:
            try:
                storage_usage = psutil.disk_usage(path["path"])
                results["storage"].append({"path": path["path"], "error": False, 
                "warn": path["warn"],
                "warn_level": path["warn_level"],
                "result": {
                    "total": storage_usage.total, "used": storage_usage.used, "free": storage_usage.free, "percent": storage_usage.percent
                }})
            except:
                results["storage"].append({"path": path["path"], "error": True, "warn": path["warn"],
                "warn_level": path["warn_level"]})
    return JsonResponse(results)