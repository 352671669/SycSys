from django.shortcuts import render
from .models import script
from blueking.component.shortcuts import get_client_by_user, get_client_by_request
from django.http import HttpResponse, JsonResponse


# Create your views here.
def excute(request):
    scripts = script.objects.all()
    return render(request, "excute.html", {"scripts": scripts})


# 获取业务
def get_business(request):
    client = get_client_by_request(request)
    businesses = client.cc.search_business()
    return JsonResponse(businesses)


# 获取主机
def get_hosts(request):
    res = {}
    res["catalogues"] = {
        "choise": "选择",
        "index": "序号",
        "ip": "IP",
        "os": "操作系统",
    }
    items = []
    client = get_client_by_request(request)
    hosts = client.cc.search_host(bk_biz_id=request.GET.get("id"))
    for index, item in enumerate(hosts["data"]["info"]):
        items.append({"choise": '<input type="radio">',
                      "index": index,
                      "ip": item["host"]["bk_host_innerip"],
                      "os": item["host"]["bk_os_name"],
                      })

    res["items"] = items
    return JsonResponse(res)
