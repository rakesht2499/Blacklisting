from django.db import IntegrityError
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from . models import Ipv4
from . serializers import ipSerializer
from blacklisting.settings import blacklist

import json


def helper():
    print("Loading all Ip's from Database")
    all_ip = Ipv4.objects.all()
    for x in all_ip:
        blacklist.add(x.ip)


def defaultView(request):
    print(request.META.get('HTTP_X_FORWARDED_FOR'))
    print(request.META.get('REMOTE_ADDR'))
    return HttpResponse("Welcome to the Blacklisting API")


def Blacklist(request):
    rq_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if blacklist.is_present(rq_ip):
        raise Http404
    return HttpResponse("Welcome to the Blacklisting API ")


@csrf_exempt
def Ipv4Api(request):
    if request.method == "GET":
        ip = Ipv4.objects.all()
        ser = ipSerializer(ip, many=True)
        resp_list = []
        for x in ser.data:
            resp_list.append(x["ip"])
        resp = {"all_ip": resp_list}
        return HttpResponse(json.dumps(resp), content_type="text/json")
    elif request.method == "POST":
        req_body = request.body.decode('utf-8')
        d = json.loads(json.loads(req_body))
        user_ip = d["ip"]
        blacklist.add(user_ip)
        try:
            Ipv4(ip=user_ip).save()
        except IntegrityError:
            pass
        return HttpResponse(201)
    elif request.method == "DELETE":
        req_body = request.body.decode('utf-8')
        d = json.loads(json.loads(req_body))
        user_ip = d["ip"]
        blacklist.remove(user_ip)
        Ipv4.objects.filter(ip=user_ip).delete()
        return HttpResponse(200)
    else:
        return HttpResponseNotAllowed()
