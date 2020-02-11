import unittest

from decouple import config

from zoopy.utils import authentication_key

class BaseTest(unittest.TestCase):
    def setUp(self):
        authentication_key(
            api_key=config('ZOOP_API_KEY'),
            marketplace_id=config('ZOOP_MARKETPLACE_ID')
        )