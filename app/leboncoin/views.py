import json

from django.shortcuts import render
from django.http import JsonResponse

from app.leboncoin.services import LeboncoinService
from app.leboncoin.models import Ad
from app.leboncoin.forms.leboncoin_api_save import SaveLeboncoinAdsForm

def leboncoin_api(_):
    return JsonResponse(json.loads(LeboncoinService.leboncoin_ads()), safe=False)

def leboncoin_api_beautify(request):
    ad_list = {'ad_list': json.loads(LeboncoinService.leboncoin_ads())}
    return render(request, 'leboncoin/leboncoin_api_beautify.html', ad_list)

def leboncoin_api_save(request):
    if request.method == 'POST':
        form = SaveLeboncoinAdsForm(request.POST)
        if form.is_valid():
            ad_list = json.loads(LeboncoinService.leboncoin_ads())
            Ad.create_ads(ad_list)
            message = "Leboncoin ads are saved by %s" % (form.cleaned_data['your_name'])
            return JsonResponse({'message': message})

    else:
        form = SaveLeboncoinAdsForm()

    return render(request, 'leboncoin/leboncoin_api_save.html', {'form': form})
