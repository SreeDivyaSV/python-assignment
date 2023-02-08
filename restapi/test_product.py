import unittest
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from products import get_product, get_products
class tests(unittest.TestCase):
    @patch('products.get_products')
    def test_getting_products(self,mock_get):
    # Configure the mock to return a response with an OK status code.
        mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
        response = get_products()

    # If the request is sent successfully, then I expect a response to be returned.
        assert_is_not_none(response)
    @patch('products.get_products')
    def test_getting_product(self,mock_get):
    # Configure the mock to return a response with an OK status code.
        mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
        response = get_product('5')

    # If the request is sent successfully, then I expect a response to be returned.
        assert_is_not_none(response)
    
if __name__ == '__main__':
    unittest.main()
