# encoding: utf-8
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "袁皓玮" # 这里填下你的名字
default_params = {"t1":5} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1":"过去5天"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv):
    """
        过去5天的净利润/过去5天的总市值
            """
    ETOP5 = dv.add_formula('ETOP5', "Ts_Sum(TTM(net_profit),%s)/Ts_Sum(total_mv,%s)"%(default_params["t1"],default_params["t1"]),
                           is_quarterly=True,
                           add_data=True)
    return ETOP5