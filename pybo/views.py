import requests
from django.http import HttpResponse
from django.shortcuts import render
from ipware import get_client_ip
import json

from pybo.models import Ipaddress


def index(request):
    # ip = get_client_ip(request)

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        print(ip)
        api = 'http://ip-api.com/json/{ip}'
        url = api.format(ip=ip)
        print(url)

        headers = {'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
                   'fields': 'district'}
        res = requests.get(url, data=headers)
        data = json.loads(res.text)

        user = Ipaddress(ipaddress=ip,
                         status=data['status'],
                         country=data['country'],
                         regionName=data['regionName'],
                         city=data['city'],
                         zip=data['zip'])

        user.save()

    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        api = 'http://ip-api.com/json/{ip}'
        url = api.format(ip=ip)
        print(url)

        headers = {'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        res = requests.get(url, data=headers)
        data = json.loads(res.text)

        print("status: ", data['status'])

    return render(request, 'mypage.html')
