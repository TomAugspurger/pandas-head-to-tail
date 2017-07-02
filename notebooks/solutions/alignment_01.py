# Option 1: The "manual way"
common = pd.Index(cpi.DATE).intersection(gdp.DATE)
rgdp = (gdp.loc[gdp.DATE.isin(common), 'GDP'].values /
        cpi.loc[cpi.DATE.isin(common), 'CPIAUCSL'])
display.display(rgdp.head())

# Option 2: "merge"
m = pd.merge(gdp, cpi, on="DATE")
rgdp = m['GDP'] / m['CPIAUCSL']
rgdp.head()
