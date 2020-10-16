import os

PATH = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(PATH, "configuration.ini"), "r", encoding='utf-8') as f:
    configuration_ini = f.read()

with open(os.path.join(PATH, "custom.py"), "r", encoding='utf-8') as f:
    custom_py = f.read()

with open(os.path.join(PATH, "train.py"), "r", encoding='utf-8') as f:
    train_py = f.read()

with open(os.path.join(PATH, "eda.py"), "r", encoding='utf-8') as f:
    eda_py = f.read()

with open(os.path.join(PATH, "score.py"), "r", encoding='utf-8') as f:
    score_py = f.read()

__all__ = [configuration_ini, custom_py, train_py, eda_py, score_py]
