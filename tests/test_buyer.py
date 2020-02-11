import time
import unittest
from zoopy import buyer
from tests.base_unittest import BaseTest
from tests.resources import buyer_data_sample


class TestBuyer(BaseTest):
    buyer = None

    def test01_list_buyers(self):
        all_buyers = buyer.list()
        self.assertIsNotNone(all_buyers)

    def test02_create_buyer(self):
        self.__class__._buyer = buyer.create(params=buyer_data_sample.BUYER)
        self.assertIsNotNone(self.__class__._buyer['id'])

    def test03_details(self):        
        details = buyer.details(str(self.__class__._buyer['id']))
        self.assertEqual(self.__class__._buyer['id'], details['id'])

    def test04_update(self):
        updated = buyer.update(buyer_id=str(self.__class__._buyer['id']),
            params={'first_name':'New name'})
        self.assertEqual('New name', updated['first_name'])

    def test05_delete(self):
        response = buyer.remove(buyer_id=str(self.__class__._buyer['id']))
        self.assertTrue(response["deleted"])

if __name__ == '__main__':
    unittest.main()