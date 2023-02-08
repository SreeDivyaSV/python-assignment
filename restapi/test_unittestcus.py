import unittest
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from customers import get_customer, get_customers
class tests(unittest.TestCase):
    @patch('customers.get_customers')
    def test_getting_customers(self,mock_get):
    # Configure the mock to return a response with an OK status code.
        mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
        response = get_customers()

    # If the request is sent successfully, then I expect a response to be returned.
        assert_is_not_none(response)
    @patch('customers.get_customer')
    def test_getting_customer(self,mock_get):
    # Configure the mock to return a response with an OK status code.
        mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
        response = get_customer('ANTON')

    # If the request is sent successfully, then I expect a response to be returned.
        assert_is_not_none(response)
    
if __name__ == '__main__':
    unittest.main()
