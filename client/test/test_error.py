# coding: utf-8

"""
    Bloom Energy Appstore

    Example API that uses an Appstore

    The version of the OpenAPI document: 1.0.0
    Contact: apiteam@swagger.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import openapi_client
from openapi_client.models.error import Error  # noqa: E501
from openapi_client.rest import ApiException

class TestError(unittest.TestCase):
    """Error unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Error
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Error`
        """
        model = openapi_client.models.error.Error()  # noqa: E501
        if include_optional :
            return Error(
                code = 56, 
                message = ''
            )
        else :
            return Error(
                code = 56,
                message = '',
        )
        """

    def testError(self):
        """Test Error"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()