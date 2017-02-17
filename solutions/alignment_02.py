gdp = gdp.set_index("DATE").squeeze()
cpi = cpi.set_index("DATE").squeeze().rename("cpi")
side_by_side(gdp.head(), cpi.head())
