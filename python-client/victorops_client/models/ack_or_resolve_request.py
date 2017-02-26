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


class AckOrResolveRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, user_name=None, incident_names=None, message=None):
        """
        AckOrResolveRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user_name': 'str',
            'incident_names': 'list[str]',
            'message': 'str'
        }

        self.attribute_map = {
            'user_name': 'userName',
            'incident_names': 'incidentNames',
            'message': 'message'
        }

        self._user_name = user_name
        self._incident_names = incident_names
        self._message = message

    @property
    def user_name(self):
        """
        Gets the user_name of this AckOrResolveRequest.

        :return: The user_name of this AckOrResolveRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this AckOrResolveRequest.

        :param user_name: The user_name of this AckOrResolveRequest.
        :type: str
        """
        if user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")

        self._user_name = user_name

    @property
    def incident_names(self):
        """
        Gets the incident_names of this AckOrResolveRequest.

        :return: The incident_names of this AckOrResolveRequest.
        :rtype: list[str]
        """
        return self._incident_names

    @incident_names.setter
    def incident_names(self, incident_names):
        """
        Sets the incident_names of this AckOrResolveRequest.

        :param incident_names: The incident_names of this AckOrResolveRequest.
        :type: list[str]
        """
        if incident_names is None:
            raise ValueError("Invalid value for `incident_names`, must not be `None`")

        self._incident_names = incident_names

    @property
    def message(self):
        """
        Gets the message of this AckOrResolveRequest.

        :return: The message of this AckOrResolveRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this AckOrResolveRequest.

        :param message: The message of this AckOrResolveRequest.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, AckOrResolveRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
