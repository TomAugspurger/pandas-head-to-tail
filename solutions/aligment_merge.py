outer = (pd.merge(gdp_bad, cpi_bad, on="DATE", how='outer')
           .sort_values("DATE"))
outer.head()