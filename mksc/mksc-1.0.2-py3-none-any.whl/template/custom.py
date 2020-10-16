import numpy as np
import pandas as pd
import re


class Custom(object):
    """
    自定义预处理类函数封装
    """
    @staticmethod
    def clean_data(feature, label):
        """
        基于单元格与行操作的数据清洗

        Args:
            feature: 待清洗特征数据框
            label: 待清洗标签序列

        Returns:
            已清洗特征数据框feature_tmp, 已清洗标签序列label_tmp
        """
        feature_tmp = feature.copy()
        label_tmp = label.copy()
        # 默认值处理
        # 单位处理
        # 正则处理
        # 业务缺失值补充
        # 业务异常值剔除
        return feature_tmp, label_tmp

    @staticmethod
    def feature_combination(feature):
        """
        基于列操作的数据清洗与特征构造

        Args:
            feature: 待清洗特征数据框

        Returns:
            已清洗特征数据框feature_tmp
        """
        feature_tmp = feature.copy()
        # 构造衍生变量
        # 日期变量处理
        return feature_tmp

    @staticmethod
    def model(feature):
        """
        自定义模型
        """