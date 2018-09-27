from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

import requests
import json

def leboncoin_api(request):
    json_adds = __leboncoin_api()
    return HttpResponse(json.dumps(json_adds), content_type='application/json')

def leboncoin_api_beautify(request):
    json_adds = __leboncoin_api()
    context = {

    }
    return render(request, 'leboncoin/index.html', context)

def __leboncoin_api():
    URL = 'https://leboncoin-api-ms.herokuapp.com/'
    return requests.get(URL).json()
