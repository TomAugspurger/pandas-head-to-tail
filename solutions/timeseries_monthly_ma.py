ma = y.rolling(4).mean()
ax = ma.plot(legend=True, label="MA[4]", figsize=(12, 4))
y.plot(ax=ax, label="Observed", legend=True);