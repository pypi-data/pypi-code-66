# coding: utf-8

"""
    TKG Kubernetes API

    This API provides to vCD tenants the means to provision (create and update) Tanzu Kubernetes Grid clusters. This is complementary to the defined-entity APIs:    GET /cloudapi/1.0.0/entities/urn:vcloud:entity:vmware.tkgcluster:1.0.0:{id} which allows to retrieve the clusters created by the API presented here. This is why you will not find here a GET operation for the corresponding entity.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TkgClusterTopologyWorkers(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_class': 'str',
        'count': 'int',
        'storage_class': 'str'
    }

    attribute_map = {
        '_class': 'class',
        'count': 'count',
        'storage_class': 'storageClass'
    }

    def __init__(self, _class=None, count=None, storage_class=None):  # noqa: E501
        """TkgClusterTopologyWorkers - a model defined in Swagger"""  # noqa: E501

        self.__class = None
        self._count = None
        self._storage_class = None
        self.discriminator = None

        self._class = _class
        self.count = count
        self.storage_class = storage_class

    @property
    def _class(self):
        """Gets the _class of this TkgClusterTopologyWorkers.  # noqa: E501

        Specifies the name of the VirtualMachineClass that describes the virtual hardware settings to be used each node in the pool. This controls the hardware available to the node (CPU and memory) as well as the requests and limits on those resources. Use a VirtualMachineClass that has been associated with the placement-policy specified above (see placementPolicy element).   # noqa: E501

        :return: The _class of this TkgClusterTopologyWorkers.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this TkgClusterTopologyWorkers.

        Specifies the name of the VirtualMachineClass that describes the virtual hardware settings to be used each node in the pool. This controls the hardware available to the node (CPU and memory) as well as the requests and limits on those resources. Use a VirtualMachineClass that has been associated with the placement-policy specified above (see placementPolicy element).   # noqa: E501

        :param _class: The _class of this TkgClusterTopologyWorkers.  # noqa: E501
        :type: str
        """
        if _class is None:
            raise ValueError("Invalid value for `_class`, must not be `None`")  # noqa: E501

        self.__class = _class

    @property
    def count(self):
        """Gets the count of this TkgClusterTopologyWorkers.  # noqa: E501

        Specifies the number of worker nodes in the cluster. A cluster with zero worker nodes can be created, allowing for a cluster with only control plane nodes. There is no hard maximum for the number of worker nodes, but a reasonable limit is 150.   # noqa: E501

        :return: The count of this TkgClusterTopologyWorkers.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TkgClusterTopologyWorkers.

        Specifies the number of worker nodes in the cluster. A cluster with zero worker nodes can be created, allowing for a cluster with only control plane nodes. There is no hard maximum for the number of worker nodes, but a reasonable limit is 150.   # noqa: E501

        :param count: The count of this TkgClusterTopologyWorkers.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def storage_class(self):
        """Gets the storage_class of this TkgClusterTopologyWorkers.  # noqa: E501

        Identifies the storage class to be used for storage of the disks which store the root file systems of the control plane nodes. Use a storage class that has been associated with the placement-policy specified above (see placementPolicy element).   # noqa: E501

        :return: The storage_class of this TkgClusterTopologyWorkers.  # noqa: E501
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this TkgClusterTopologyWorkers.

        Identifies the storage class to be used for storage of the disks which store the root file systems of the control plane nodes. Use a storage class that has been associated with the placement-policy specified above (see placementPolicy element).   # noqa: E501

        :param storage_class: The storage_class of this TkgClusterTopologyWorkers.  # noqa: E501
        :type: str
        """
        if storage_class is None:
            raise ValueError("Invalid value for `storage_class`, must not be `None`")  # noqa: E501

        self._storage_class = storage_class

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TkgClusterTopologyWorkers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
