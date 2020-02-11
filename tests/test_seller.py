import os, hashlib
import unittest
from zoopy import seller
from tests.base_unittest import BaseTest

from tests.resources import seller_data_sample

class TestSeller(BaseTest):
    _seller_individual = None
    _seller_business = None
    _document = None

    def test01_list_sellers(self):
        all_sellers = seller.list()
        self.assertIsNotNone(all_sellers)

    def test02_create_seller_individual(self):
        self.__class__._seller_individual = seller.create(params=seller_data_sample.SELLER_INDIVIDUAL, 
            seller_type='individual')
        self.assertIsNotNone(self.__class__._seller_individual['id'])

    def test03_create_seller_business(self):
        self.__class__._seller_business = seller.create(params=seller_data_sample.SELLER_BUSINESS, 
            seller_type='business')
        self.assertIsNotNone(self.__class__._seller_business['id'])

    def test04_details_individual(self):
        details = seller.details(str(self.__class__._seller_individual['id']))
        self.assertEqual(self.__class__._seller_individual['id'], details['id'])

    def test05_details_business(self):
        details = seller.details(str(self.__class__._seller_business['id']))
        self.assertEqual(self.__class__._seller_business['id'], details['id'])

    def test06_update_individual(self):
        updated = seller.update(seller_id=str(self.__class__._seller_individual['id']),
            seller_type='individual', params={'first_name':'New name'})
        self.assertEqual('New name', updated['first_name'])

    def test07_update_business(self):
        updated = seller.update(seller_id=str(self.__class__._seller_business['id']),
            seller_type='business', params={'business_name':'New name'})
        self.assertEqual('New name', updated['business_name'])

    def test08_create_document(self):
        test_dir = os.path.dirname(__file__)
        document_path = 'resources/document.jpg'
        
        image = open(os.path.join(test_dir, document_path), 'rb')
        self.__class__._document = seller.add_documment(seller_id=str(self.__class__._seller_individual['id']),
            params={'category':'identificacao'}, files={"file": image})

        image.close()
        self.assertEqual('identificacao', self.__class__._document['category'])

    def test09_get_documents(self):
        documents = seller.get_documents(seller_id=str(self.__class__._seller_individual['id']))
        self.assertNotEqual(documents['items'], [])

    #Retornando vazio na zoop
    # def test10_update_document(self):
    #     document = seller.update_document(document_id=str(self.__class__._document['id']),
    #         params={'description':'anderson', 'id':str(self.__class__._document['id'])})
    #     self.assertEqual('anderson', document['category'])

    def test10_get_transfers(self):
        transfers = seller.transfers(seller_id=str(self.__class__._seller_business['id']))
        self.assertEqual(transfers['items'], [])

    def test11_delete_inidvidual(self):
        response = seller.remove(seller_id=str(self.__class__._seller_individual['id']))
        self.assertTrue(response["deleted"])

    def test11_delete_business(self):
        response = seller.remove(seller_id=str(self.__class__._seller_business['id']))
        self.assertTrue(response["deleted"])


if __name__ == '__main__':
    unittest.main()