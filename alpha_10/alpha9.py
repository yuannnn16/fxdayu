# encoding: utf-8
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "袁皓玮" # 这里填下你的名字
default_params = {"t1":30,"t2":600} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1":"过去30天","t2":"过去600天"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv):
    """
       30日总成交量/两年总成交量乘-1
            """
    alpha9 = dv.add_formula('alpha9', "-Ts_Sum(volume,%s)/Ts_Sum(volume,%s)"%(default_params["t1"],default_params["t2"]),
                           is_quarterly=False,
                           add_data=True)
    return alpha9