import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import auc, roc_curve, accuracy_score, recall_score
import matplotlib.pyplot as plt
from mksc.selection import model_method as mms
from mksc.selection import statistics_method as sms
from mksc.process import process as pp
from mksc.process import preprocess as pr
from mksc.process import woe_process as pw
import custom


def feature_engineering(feature, label):
    """
    特征工程过程函数：
    1. 特征组合
    2. 基于统计特性特征选择：缺失率、唯一率、众数比例
    3. 极端值处理
    4. TODO 异常值处理
    5. 缺失值处理
    6. COMMENT 归一化处理
    7. COMMENT 正态化处理
    8. 最优分箱
    9. IV筛选
    10. TODO PSI筛选
    11. 相关性筛选
    12. woe转化
    13. 逐步回归筛选

    Args:
        feature: 待处理特征数据框
        label: 特征数据框对应标签

    Returns:
        feature： 已完成特征工程的数据框
    """
    # 自定义特征组合模块
    feature = custom.Custom.feature_combination(feature)

    # 基于缺失率、唯一率、众数比例统计特征筛选
    missing_value = sms.get_missing_value(feature)
    distinct_value = sms.get_distinct_value(feature)
    unique_value = sms.get_unique_value(feature)
    feature.drop(set(missing_value['drop'] + distinct_value['drop'] + unique_value['drop']), axis=1, inplace=True)

    # 极端值处理
    feature, abnormal_value = pp.fix_abnormal_value(feature)

    # 缺失值处理
    feature, missing_filling = pp.fix_missing_value(feature)

    # 归一化处理
    # feature = pp.fix_scaling(feature)

    # 正态化处理
    # feature, standard_lambda = pp.fix_standard(feature)

    # 数值特征最优分箱，未处理的变量，暂时退出模型
    bin_result, iv_result, woe_result, woe_adjust_result = pw.binning(label, feature)
    bin_error_drop = bin_result['error'] + woe_adjust_result

    # IV筛选
    iv_drop = list(filter(lambda x: iv_result[x] < 0.02, iv_result))
    feature.drop(iv_drop + bin_error_drop, inplace=True, axis=1)

    # 相关性筛选
    cor_drop = sms.get_cor_drop(feature, iv_result)
    feature.drop(cor_drop, inplace=True, axis=1)

    # woe转化
    feature = pw.woe_transform(feature, woe_result, bin_result)

    # 逐步回归筛选
    feature_selected = mms.stepwise_selection(feature, label)
    feature = feature[feature_selected]

    # 中间结果保存
    result = {"missing_value": missing_value,
              "distinct_value": distinct_value,
              "unique_value": unique_value,
              "abnormal_value": abnormal_value,
              "missing_filling": missing_filling,
              "bin_result": bin_result,
              "iv_result": iv_result,
              "woe_result": woe_result,
              "woe_adjust_result": woe_adjust_result,
              "bin_error_drop": bin_error_drop,
              "iv_drop": iv_drop,
              "cor_drop": cor_drop,
              "feature_selected": feature_selected
              }
    with open('result/feature_engineering.pickle', 'wb') as f:
        f.write(pickle.dumps(result))
    return feature


def training(x_train, y_train, x_test, y_test, x_valid, y_valid):
    """
    模型训练过程函数
    1. 训练
    2. 预测
    3. 评估
    4. TODO 模型可选

    Args:
        x_train: 训练集特征
        y_train: 训练集标签
        x_test: 测试集特征
        y_test: 测试集标签
        x_valid: 验证集特征
        y_valid: 验证集标签
    """
    model = LogisticRegression()
    model.fit(x_train, y_train)

    # 预测结果
    predict_train = model.predict(x_train)
    predict_valid = model.predict(x_valid)
    predict_test = model.predict(x_test)

    # 模型评估
    acu_train = accuracy_score(y_train, predict_train)
    acu_valid = accuracy_score(y_valid, predict_valid)
    acu_test = accuracy_score(y_test, predict_test)

    sen_train = recall_score(y_train, predict_train, pos_label=1)
    sen_valid = recall_score(y_valid, predict_valid, pos_label=1)
    sen_test = recall_score(y_test, predict_test, pos_label=1)

    spe_train = recall_score(y_train, predict_train, pos_label=0)
    spe_valid = recall_score(y_valid, predict_valid, pos_label=0)
    spe_test = recall_score(y_test, predict_test, pos_label=0)
    print(f'模型准确率：验证 {acu_valid * 100:.2f}%	训练 {acu_train * 100:.2f}%	测试 {acu_test * 100:.2f}%')
    print(f'正例覆盖率：验证 {sen_valid * 100:.2f}%	训练 {sen_train * 100:.2f}%	测试 {sen_test * 100:.2f}%')
    print(f'负例覆盖率：验证 {spe_valid * 100:.2f}%	训练 {spe_train * 100:.2f}%	测试 {spe_test * 100:.2f}%')

    # K-s & roc
    predict_train_prob = np.array([i[1] for i in model.predict_proba(x_train)])
    fpr, tpr, thresholds = roc_curve(y_train.values, predict_train_prob, pos_label=1)
    auc_score = auc(fpr, tpr)
    w = tpr - fpr
    ks_score = w.max()
    ks_x = fpr[w.argmax()]
    ks_y = tpr[w.argmax()]
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label='AUC=%.5f' % auc_score)
    ax.set_title('Receiver Operating Characteristic')
    ax.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6))
    ax.plot([ks_x, ks_x], [ks_x, ks_y], '--', color='red')
    ax.text(ks_x, (ks_x + ks_y) / 2, '  KS=%.5f' % ks_score)
    ax.legend()
    fig.savefig("result/ks_roc.png")

    # 模型保存
    coefs = dict(list(zip(x_train.columns, list(model.coef_[0]))) + [("intercept_", model.intercept_[0])])
    with open('result/model.pickle', 'wb') as f:
        f.write(pickle.dumps(model))
    with open('result/coefs.pickle', 'wb') as f:
        f.write(pickle.dumps(coefs))


def main():
    """
    项目训练程序入口
    """
    # 加载数据、变量类型划分、特征集与标签列划分
    data = pr.load_data()
    numeric_var, category_var, datetime_var, label_var = pr.get_variable_type()
    feature = data[numeric_var + category_var + datetime_var]
    label = data[label_var]

    # 自定义数据清洗
    feature, label = custom.Custom.clean_data(feature, label)

    # 数据类型转换
    feature[numeric_var] = feature[numeric_var].astype('float')
    feature[category_var] = feature[category_var].astype('object')
    feature[datetime_var] = feature[datetime_var].astype('datetime64')

    # 特征工程
    feature = feature_engineering(feature, label)

    # 数据集划分
    x_train, x_valid_test, y_train, y_valid_test = train_test_split(feature, label, test_size=0.4, random_state=0)
    x_valid, x_test, y_valid, y_test = train_test_split(x_valid_test, y_valid_test, test_size=0.5, random_state=0)

    # 模型训练
    training(x_train, y_train, x_test, y_test, x_valid, y_valid)


if __name__ == "__main__":
    main()
