import unittest
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from orders import get_order, get_orders
class tests(unittest.TestCase):
    @patch('orders.get_orders')
    def test_getting_orders(self,mock_get):
    # Configure the mock to return a response with an OK status code.
        mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
        response = get_orders()

    # If the request is sent successfully, then I expect a response to be returned.
        assert_is_not_none(response)
    @patch('orders.get_order')
    def test_getting_order(self,mock_get):
    # Configure the mock to return a response with an OK status code.
        mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
        response = get_order('10249')

    # If the request is sent successfully, then I expect a response to be returned.
        assert_is_not_none(response)
    
if __name__ == '__main__':
    unittest.main()
