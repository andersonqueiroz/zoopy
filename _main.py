# from zoopy.models import Marketplace, Seller, Owner, Address, Buyer, Transaction
from zoopy.utils import authentication_key
import zoopy

authentication_key(
        api_key='TEST_API_KEY', 
        marketplace_id="MARKETPLACE_ID"
    )

results = zoopy.plan.list(is_beta=True)

print(results)
