# coding: utf-8

"""
    VictorOps API

    This API allows you to interact with the VictorOps platform in various ways. Your account may be limited to a total number of API calls per month. Also, some of these API calls have rate limits.  NOTE: In this documentation when creating a sample curl request (clicking the TRY IT OUT! button), in some API viewing interfaces, the '@' in an email address may be encoded. Please note that the REST endpoints will not process the encoded version. Make sure that the encoded character '%40' is changed to its unencoded form before submitting the curl request. 

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import victorops_client
from victorops_client.rest import ApiException
from victorops_client.models.create_incident_request import CreateIncidentRequest


class TestCreateIncidentRequest(unittest.TestCase):
    """ CreateIncidentRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateIncidentRequest(self):
        """
        Test CreateIncidentRequest
        """
        model = victorops_client.models.create_incident_request.CreateIncidentRequest()


if __name__ == '__main__':
    unittest.main()
