def run_formula(dv):
    variance120 = dv.add_formula('variance120', "Covariance(Delta(close,1),Delta(close,1),120)",
                                 is_quarterly=False,
                                 add_data=True)
    return variance120