def run_formula(dv):
    PEHIST60 = dv.add_formula('PEHIST60', "PE/Ts_Mean(PE,60)",
                              is_quarterly=False,
                              add_data=True)
    return PEHIST60