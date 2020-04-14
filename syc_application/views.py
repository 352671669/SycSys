from django.shortcuts import render
from .models import script, ExcuteInfo
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


# 获取脚本
def get_scripts(request):
    client = get_client_by_request(request)
    scripts = client.job.get_script_list(bk_biz_id=3)
    return JsonResponse(scripts)


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
    hosts = client.cc.search_host(bk_biz_id=3)
    for index, item in enumerate(hosts["data"]["info"]):
        items.append({"choise": '<input type="radio">',
                      "index": index,
                      "ip": item["host"]["bk_host_innerip"],
                      "os": item["host"]["bk_os_name"],
                      })

    res["items"] = items
    return JsonResponse(res)


def excute_script(request):
    bk_biz_id = request.POST.get("businessId")
    script_id = request.POST.get("scriptId")
    client = get_client_by_request(request)
    kwargs = {
        "bk_biz_id": 3,
        "script_id": script_id,
        "ip_list": [{
            "bk_cloud_id": 0,
            "ip": "10.0.2.15"
        }],
        "account": "root"
    }
    result = client.job.fast_execute_script(kwargs)
    excuteInfo = ExcuteInfo(context=result)
    excuteInfo.save()
    # print(str(result))
    return JsonResponse(result)
