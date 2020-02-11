import unittest
from zoopy import token, bank_account

from tests.base_unittest import BaseTest
from tests.resources import token_data_sample

class TestBankAccount(BaseTest):
    
    def setUp(self):
        super(TestBankAccount, self).setUp()
        self.__class__._bank_account = token.create(token_type='bank_account',
            params=token_data_sample.TOKEN_BANK_ACCOUNT).get('bank_account')

    def test01_list_bank_accounts(self):
        all_bank_accounts = bank_account.list()
        self.assertIsNotNone(all_bank_accounts)

    def test01_details_bank_account(self):
        details = bank_account.details(bank_account_id=self.__class__._bank_account['id'])        
        self.assertEqual(self.__class__._bank_account['id'], details['id'])

    # def test02_update_bank_account(self):
    #     update = bank_account.update(bank_account_id=self.__class__._bank_account['id'],
    #         params={'is_active': 'True'})
    #     print(update)
    #     self.assertTrue(update['is_active'])

    def test02_delete_bank_account(self):
        response = bank_account.remove(bank_account_id=self.__class__._bank_account['id'])        
        self.assertTrue(response["deleted"])

if __name__ == '__main__':
    unittest.main()