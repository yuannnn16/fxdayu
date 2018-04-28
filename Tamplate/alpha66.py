def run_formula(dv):
    alpha66 = dv.add_formula('alpha66', "(close-Ts_Mean(close,6))/Ts_Mean(close,6)*100",
                             is_quarterly=False,
                             add_data=True)
    return alpha66