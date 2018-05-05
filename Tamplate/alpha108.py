# encoding: utf-8
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "袁皓玮" # 这里填下你的名字
default_params = {"t1":2,"t2":120,"t3":6} # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {"t1":"过去2天","t2":"过去120天","t3":"过去6天"} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv):
    """
     (最高价在过去两日增长的排名)^(成交量加权平均价与过去120天的平均成交量在过去6天的相关系数排名)*-1
           """
    alpha108 = dv.add_formula('alpha108',
                              "((Rank(high-Ts_Min(high,%s)))^(Rank(Correlation(vwap,Ts_Mean(volume,%s),%s)))*-1)"%(default_params["t1"],default_params["t2"],default_params["t3"]),
                              is_quarterly=False,
                              add_data=True)
    return alpha108