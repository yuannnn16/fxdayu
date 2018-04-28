def run_formula(dv):
    alpha108 = dv.add_formula('alpha108',
                              "((Rank(high-Ts_Min(high,2)))^(Rank(Correlation(vwap,Ts_Mean(volume,120),6)))*-1)",
                              is_quarterly=False,
                              add_data=True)
    return alpha108