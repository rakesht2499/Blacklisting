from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
from . models import Ipv4
from . serializers import ipSerializer


def defaultView(request):
    print(request.META.get('HTTP_X_FORWARDED_FOR'))
    print(request.META.get('REMOTE_ADDR'))
    return HttpResponse("Welcome to the Blacklisting API")


@csrf_exempt
def Ipv4Api(request):
    if request.method == "GET":
        ip = Ipv4.objects.all()
        ser = ipSerializer(ip, many=True)
        return render(request, "getrequest.html", {"ip_in_db": ser.data})
    elif request.method == "POST":
        req_body = request.body.decode('utf-8')
        d = json.loads(json.loads(req_body))
        ip = Ipv4(ip=d["ip"])
        try:
            ip.save()
        except IntegrityError:
            return render(request, "getrequest.html", {'ip_in_db': "Data Already Exist"})
        return render(request, "getrequest.html", {"ip_in_db": ipSerializer(Ipv4.objects.all(), many=True).data})
    elif request.method == "PUT":
        req_body = request.body.decode('utf-8')
        ip = json.loads(json.loads(req_body))
        same = get_object_or_404(Ipv4, ip=ip['ip'])
        Ipv4(ip=ip['newip'], id=same.id).save()
        return HttpResponse(200)
    elif request.method == "DELETE":
        req_body = request.body.decode('utf-8')
        ip = json.loads(json.loads(req_body))
        get_object_or_404(Ipv4, ip=ip['ip']).delete()
        print("Inside the DELETE Function")
        return HttpResponse(200)
    else:
        return HttpResponseNotAllowed()
