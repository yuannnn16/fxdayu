def run_formula(dv):
    VEMA5 = dv.add_formula('VEMA5_J', "Ta('EMA',0,volume,volume,volume,volume,volume,5)",
                           is_quarterly=False,
                             add_data=True)
    return VEMA5