import json

from django.test import SimpleTestCase
from services import LeboncoinService


class LeboncoinServiceTests(SimpleTestCase):

    def test_sort_by_price(self):
        json_adds = open(
            "app/leboncoin/json_examples/data.json"
        )
        json_adds_sorted_by_price = open(
            "app/leboncoin/json_examples/data_sorted_by_price.json"
        )

        json_list = json.load(json_adds)
        sorted_by_price = LeboncoinService.sort_by_price(json_list)

        self.assertListEqual(
            sorted_by_price, json.load(json_adds_sorted_by_price)
        )
