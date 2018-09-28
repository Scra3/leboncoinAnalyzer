import json

from django.http import HttpResponse
from django.shortcuts import render

from app.leboncoin.services import LeboncoinService

def leboncoin_api(_):
    return HttpResponse(
        LeboncoinService.leboncoin_ads(), content_type='application/json'
    )

def leboncoin_api_beautify(request):
    context = {'ad_list': json.loads(LeboncoinService.leboncoin_ads())}
    return render(request, 'leboncoin/index.html', context)
