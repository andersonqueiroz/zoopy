import unittest
from zoopy import token, seller

from tests.base_unittest import BaseTest
from tests.resources import token_data_sample, seller_data_sample

class TestToken(BaseTest):
    _token_card = None
    _token_bank_account = None

    def test01_create_token_card(self):
        self.__class__._token_card = token.create(token_type='card',
            params=token_data_sample.TOKEN_CARD)
        self.assertIsNotNone(self.__class__._token_card['id'])

    def test02_create_token_bank_account(self):
        self.__class__._token_bank_account = token.create(token_type='bank_account',
            params=token_data_sample.TOKEN_BANK_ACCOUNT)
        self.assertIsNotNone(self.__class__._token_bank_account['id'])

    def test03_details_token_card(self):
        details = token.details(str(self.__class__._token_card['id']))
        self.assertEqual(self.__class__._token_card['id'], details['id'])

    # def test04_details_token_bank_account(self):
    #     details = token.details(str(self.__class__._token_bank_account['id']))
    #     self.assertEqual(self.__class__._token_bank_account['id'], details['id'])

    def test05_attach_bank_account(self):
        seller_id = seller.create(params=seller_data_sample.SELLER_INDIVIDUAL, 
            seller_type='individual').get('id')

        attach = token.attach_bank_account(seller_id=seller_id,
            token_id=self.__class__._token_bank_account['id'])

        seller.remove(seller_id=seller_id)
        self.assertEqual(seller_id, attach['customer'])

    def test06_attach_card(self):
        seller_id = seller.create(params=seller_data_sample.SELLER_INDIVIDUAL, 
            seller_type='individual').get('id')

        attach = token.attach_card(seller_id=seller_id,
            token_id=self.__class__._token_card['id'])

        seller.remove(seller_id=seller_id)
        self.assertEqual(seller_id, attach['customer'])

if __name__ == '__main__':
    unittest.main()