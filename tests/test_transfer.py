import unittest
from tests.base_unittest import BaseTest

from zoopy import transfer, seller
from tests.resources import transfer_data_sample, seller_data_sample

class TestTransfer(BaseTest):
    
    def test01_list_transfers(self):
        all_trasnfers = transfer.list_all()
        self.assertIsNotNone(all_trasnfers)

if __name__ == '__main__':
    unittest.main()