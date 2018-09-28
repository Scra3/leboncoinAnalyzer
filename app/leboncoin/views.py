import json

from django.http import HttpResponse
from django.shortcuts import render

from app.leboncoin.services import LeboncoinService


def leboncoin_api(_):
    return HttpResponse(
        LeboncoinService.leboncoin_adds(), content_type='application/json'
    )

def leboncoin_api_beautify(request):
    context = {'add_list': json.loads(LeboncoinService.leboncoin_adds())}
    return render(request, 'leboncoin/index.html', context)
