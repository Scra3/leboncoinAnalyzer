from django.test import SimpleTestCase
from django.test import Client

class LeboncoinViewsTests(SimpleTestCase):

    def test_leboncoin_api_view(self):
        self.__test_leboncoin_api('/leboncoin/api', 200)

    def test_leboncoin_api_beautify_view(self):
        self.__test_leboncoin_api('/leboncoin/api/beautify', 200)

    def test_leboncoin_api_save_post_view(self):
        self.__test_leboncoin_api('/leboncoin/api/save', 200, params={'your_name': "alban"})

    def test_leboncoin_api_save_get_view(self):
        self.__test_leboncoin_api('/leboncoin/api/save', 200)

    def __test_leboncoin_api(self, url, code, params=None):
        response = Client().post(url, params=params)
        self.assertEqual(response.status_code, code)
