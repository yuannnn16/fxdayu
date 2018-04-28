def run_formula(dv):
   ROE_J=dv.add_formula('ROE_J',"TTM(net_profit)/net_assets",
                        is_quarterly=True,
                        add_data=True)
   return ROE_J