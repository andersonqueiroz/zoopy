import unittest
from tests.base_unittest import BaseTest

from zoopy import transaction, buyer, seller
from tests.resources import transaction_data_sample, buyer_data_sample, seller_data_sample

class TestTransaction(BaseTest):
    
    def test01_list_transactions(self):
        all_transactions = transaction.list()
        self.assertIsNotNone(all_transactions)

    def test01_create_detail_update__void_transaction(self):
        buyer_id = buyer.create(buyer_data_sample.BUYER).get('id')
        transaction_data = transaction_data_sample.TRANSACTION
        transaction_data['on_behalf_of'] = "7355b0f00ade4e5d88648c5f8f02681b"
        transaction_data['customer'] = buyer_id

        new_transaction = transaction.create(params=transaction_data)
        self.assertIsNotNone(new_transaction['id'])

        details = transaction.details(str(new_transaction['id']))
        self.assertEqual(new_transaction['id'], details['id'])        
    
        updated = transaction.update(transaction_id=new_transaction['id'],
            params={'description':'New description'})
        self.assertEqual('New description', updated['description'])

if __name__ == '__main__':
    unittest.main()