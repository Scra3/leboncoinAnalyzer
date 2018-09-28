import json
import requests

from app.configs import Configs

class LeboncoinService:

    @staticmethod
    def leboncoin_adds():
        sorted_adds = LeboncoinService.sort_by_price(
            LeboncoinService.leboncoin_api_adds()
        )
        return json.dumps(sorted_adds)

    @staticmethod
    def leboncoin_api_adds():
        try:
            return requests.get(Configs.LEBONCOIN_URL).json()
        except requests.exceptions.HTTPError:
            print("Can't access to the leboncoin api")

    @staticmethod
    def sort_by_price(json_list):
        return sorted(json_list, key=lambda x: x['price'])
