from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=5000)
    description = models.TextField(default="No desc")
    price = models.FloatField(max_length=200, default=0.0)
    city_label = models.CharField(max_length=50)
    date = models.CharField(max_length=200)

    @staticmethod
    def create_ads(ad_list):
        for leboncoin_ad in ad_list:
            Ad.objects.create(title=leboncoin_ad['title'],
                              description=leboncoin_ad['description'],
                              price=leboncoin_ad['price'],
                              date=leboncoin_ad['date'],
                              city_label=leboncoin_ad['location']['city_label'])
