#!/usr/bin/python
#
# Copyright 2018-2020 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.2.0-rc4
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from polyaxon_sdk.configuration import Configuration


class V1MetricEarlyStopping(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "kind": "str",
        "metric": "str",
        "value": "str",
        "optimization": "V1Optimization",
        "policy": "object",
    }

    attribute_map = {
        "kind": "kind",
        "metric": "metric",
        "value": "value",
        "optimization": "optimization",
        "policy": "policy",
    }

    def __init__(
        self,
        kind="metric_early_stopping",
        metric=None,
        value=None,
        optimization=None,
        policy=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """V1MetricEarlyStopping - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._metric = None
        self._value = None
        self._optimization = None
        self._policy = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if metric is not None:
            self.metric = metric
        if value is not None:
            self.value = value
        if optimization is not None:
            self.optimization = optimization
        if policy is not None:
            self.policy = policy

    @property
    def kind(self):
        """Gets the kind of this V1MetricEarlyStopping.  # noqa: E501


        :return: The kind of this V1MetricEarlyStopping.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1MetricEarlyStopping.


        :param kind: The kind of this V1MetricEarlyStopping.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metric(self):
        """Gets the metric of this V1MetricEarlyStopping.  # noqa: E501

        Metric name to use for early stopping.  # noqa: E501

        :return: The metric of this V1MetricEarlyStopping.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this V1MetricEarlyStopping.

        Metric name to use for early stopping.  # noqa: E501

        :param metric: The metric of this V1MetricEarlyStopping.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def value(self):
        """Gets the value of this V1MetricEarlyStopping.  # noqa: E501

        Metric value to use for the condition.  # noqa: E501

        :return: The value of this V1MetricEarlyStopping.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V1MetricEarlyStopping.

        Metric value to use for the condition.  # noqa: E501

        :param value: The value of this V1MetricEarlyStopping.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def optimization(self):
        """Gets the optimization of this V1MetricEarlyStopping.  # noqa: E501


        :return: The optimization of this V1MetricEarlyStopping.  # noqa: E501
        :rtype: V1Optimization
        """
        return self._optimization

    @optimization.setter
    def optimization(self, optimization):
        """Sets the optimization of this V1MetricEarlyStopping.


        :param optimization: The optimization of this V1MetricEarlyStopping.  # noqa: E501
        :type: V1Optimization
        """

        self._optimization = optimization

    @property
    def policy(self):
        """Gets the policy of this V1MetricEarlyStopping.  # noqa: E501


        :return: The policy of this V1MetricEarlyStopping.  # noqa: E501
        :rtype: object
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this V1MetricEarlyStopping.


        :param policy: The policy of this V1MetricEarlyStopping.  # noqa: E501
        :type: object
        """

        self._policy = policy

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, V1MetricEarlyStopping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1MetricEarlyStopping):
            return True

        return self.to_dict() != other.to_dict()
