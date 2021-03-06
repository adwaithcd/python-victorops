# coding: utf-8

"""
    VictorOps API

    This API allows you to interact with the VictorOps platform in various ways. Your account may be limited to a total number of API calls per month. Also, some of these API calls have rate limits.  NOTE: In this documentation when creating a sample curl request (clicking the TRY IT OUT! button), in some API viewing interfaces, the '@' in an email address may be encoded. Please note that the REST endpoints will not process the encoded version. Make sure that the encoded character '%40' is changed to its unencoded form before submitting the curl request. 

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse200(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, devices=None, emails=None, phones=None):
        """
        InlineResponse200 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'devices': 'list[ContactDevice]',
            'emails': 'list[UserContact]',
            'phones': 'list[UserContact]'
        }

        self.attribute_map = {
            'devices': 'devices',
            'emails': 'emails',
            'phones': 'phones'
        }

        self._devices = devices
        self._emails = emails
        self._phones = phones

    @property
    def devices(self):
        """
        Gets the devices of this InlineResponse200.

        :return: The devices of this InlineResponse200.
        :rtype: list[ContactDevice]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """
        Sets the devices of this InlineResponse200.

        :param devices: The devices of this InlineResponse200.
        :type: list[ContactDevice]
        """

        self._devices = devices

    @property
    def emails(self):
        """
        Gets the emails of this InlineResponse200.

        :return: The emails of this InlineResponse200.
        :rtype: list[UserContact]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """
        Sets the emails of this InlineResponse200.

        :param emails: The emails of this InlineResponse200.
        :type: list[UserContact]
        """

        self._emails = emails

    @property
    def phones(self):
        """
        Gets the phones of this InlineResponse200.

        :return: The phones of this InlineResponse200.
        :rtype: list[UserContact]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """
        Sets the phones of this InlineResponse200.

        :param phones: The phones of this InlineResponse200.
        :type: list[UserContact]
        """

        self._phones = phones

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
