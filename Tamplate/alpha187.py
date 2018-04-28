def run_formula(dv):
    alpha187 = dv.add_formula('alpha187', "Ts_Sum(If(open<=Delay(open,1),0,Max((high-open),(open<=Delay(open,1)))),20)",
                              is_quarterly=False,
                              add_data=True)
    return alpha187