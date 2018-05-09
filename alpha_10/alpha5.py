# encoding: utf-8
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "袁皓玮" # 这里填下你的名字
default_params = {"t1":30} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1":"过去30天"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv):
    """
        30天成交量方差
            """
    alpha5 = dv.add_formula('alpha5', "-StdDev(volume,%s)"%default_params["t1"],
                           is_quarterly=False,
                           add_data=True)
    return alpha5