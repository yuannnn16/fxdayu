# encoding: utf-8
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "袁皓玮" # 这里填下你的名字
default_params = {"t1":20} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1":"过去20天"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv):
    """
        每日最高价减最低价与开盘价一日涨幅的最大值的20日累计，若涨幅为负则该最大值为0
               """
    alpha187 = dv.add_formula('alpha187', "Ts_Sum(If(open<=Delay(open,1),0,Max((high-open),(open-Delay(open,1)))),%s)"%default_params["t1"],
                              is_quarterly=False,
                              add_data=True)
    return alpha187