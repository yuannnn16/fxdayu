# encoding: utf-8
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "袁皓玮" # 这里填下你的名字
default_params = {} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv):
    """
        净利润/股东权益
            """
    ROEWeighted=dv.add_formula('ROE_J',"TTM(net_profit)/net_assets",
                        is_quarterly=True,
                        add_data=True)

    return ROEWeighted