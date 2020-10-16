import numpy as np
from scipy.stats import boxcox


def fix_abnormal_value(feature, threshold=0.05):
    """
    修正数据框中的数值型变量中的异常值

    Args:
        feature: 待修正的数据框
        threshold: 异常值替换阈值

    Returns:
        feature: 已处理数据框
        abnormal_value: 异常值统计结果
    """
    numeric_var = feature.select_dtypes(exclude=['object', 'datetime']).columns
    abnormal_value = {'result': {}, 'replace': []}
    for c in numeric_var:
        sm = feature[c].describe()
        iqr = sm['75%'] - sm['25%']
        min_ = sm['25%'] - 1.5*iqr
        max_ = sm['75%'] + 1.5*iqr
        abnormal_value_indexes = list(feature.loc[(feature[c] <= min_) | (feature[c] >= max_)].index)
        abnormal_value_length = len(abnormal_value_indexes)
        abnormal_value_rate = abnormal_value_length/feature[c].count()
        abnormal_value['result'][c] = {'abnormal_value_list': abnormal_value_indexes, 
                                       'abnormal_value_length': abnormal_value_length, 
                                       'abnormal_value_rate': abnormal_value_rate,
                                       'max': max_,
                                       'min': min_}
        if abnormal_value_rate <= threshold:
            abnormal_value['replace'].append(c)
            feature.loc[:, c] = feature.loc[:, c].apply(lambda x: x if (x < max_) & (x > min_) else np.nan)
    return feature, abnormal_value

def fix_missing_value(feature, threshold=0.05):
    """
    修正数据框中的数值型变量中的缺失值

    Args:
        feature: 待修正的数据框
        threshold: 缺失值替换阈值

    Returns:
        feature: 已处理数据框
        missing_filling: 缺失值统计结果
    """
    numeric_var = feature.select_dtypes(exclude=['object', 'datetime']).columns
    missing_filling = {'result': {}, 'replace': []}
    for c in feature:
        missing_rate = feature[c].isna().sum()/len(feature)
        if missing_rate <= threshold and missing_rate:
            missing_filling['result'][c] = {'fill_number': feature[c].mean(), 'missing_value_rate': missing_rate}
            missing_filling['replace'].append(c)
            if c in numeric_var:
                feature[c].fillna(missing_filling['result'][c], inplace=True)
            else:
                feature[c].fillna(feature[c].mode(), inplace=True)
    return feature, missing_filling

def fix_scaling(feature):
    """
    对数据框中的数据进行中性化处理

    Args:
        feature: 待处理的数据框

    Returns:
        feature: 已处理数据框
    """
    numeric_var = feature.select_dtypes(exclude=['object', 'datetime']).columns
    for c in numeric_var:
        sm = feature[c].describe()
        feature[c] = feature[c].apply(lambda x: (x - sm['mean'])/sm['std'] if x else x)
    return feature

def fix_standard(feature):
    """
    对数据框中的数据进行正态化处理

    Args:
        feature: 待处理的数据框

    Returns:
        feature: 已处理数据框
        standard_lambda: 对应特征的lambda值
    """
    numeric_var = feature.select_dtypes(exclude=['object', 'datetime']).columns
    standard_lambda = {}
    for c in numeric_var:
        feature[c], lambda_ = boxcox(feature[c]+0.5)
        standard_lambda[c] = lambda_
    return feature, standard_lambda
