def run_formula(dv):
    ETOP5 = dv.add_formula('ETOP5', "Ts_Sum(TTM(net_profit),5)/Ts_Sum(total_mv,5)",
                           is_quarterly=True,
                           add_data=True)
    return ETOP5