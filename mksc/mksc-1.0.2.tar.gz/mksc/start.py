import sys
import os
from mksc.template import configuration_ini, custom_py, train_py, eda_py, score_py

def make_workspace(name):
    """
    创建项目的工作目录与脚本文件

    Args:
        name: 项目名
    """

    if os.path.exists(name):
        return f"Folder [{name}] is exists already, Please check out the work path"
    os.mkdir(name)
    os.mkdir(os.path.join(name, "conf"))
    os.mkdir(os.path.join(name, "data"))
    os.mkdir(os.path.join(name, "log"))
    os.mkdir(os.path.join(name, "model"))
    os.mkdir(os.path.join(name, "result"))

    with open(os.path.join(name, "custom.py"), "w", encoding='utf-8') as f:
        f.write(custom_py)
        
    with open(os.path.join(name, "eda.py"), "w", encoding='utf-8') as f:
        f.write(eda_py)

    configuration_ini_tmp = configuration_ini % (os.path.join(os.getcwd(), name),
                                                 os.path.join(os.getcwd(), name, "data"),
                                                 os.path.join(os.getcwd(), name, "result")
                                                 )
    with open(os.path.join(name, "conf", "configuration.ini"), "w", encoding='utf-8') as f:
        f.write(configuration_ini_tmp)

    with open(os.path.join(name, "train.py"), "w", encoding='utf-8') as f:
        f.write(train_py)        

    with open(os.path.join(name, "score.py"), "w", encoding='utf-8') as f:
        f.write(score_py)

def main():
    """
    命令行工具程序主入口
    """
    if len(sys.argv) == 1:
        return "CMD FORMAT: \n\tmksc project_name1 project_name2 ...\nPlease delivery one argument at least"
    else:
        for project_name in sys.argv[1:]:
            make_workspace(project_name)


if __name__ == "__main__":
    main()
