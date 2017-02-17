per_cap = (df.groupby(df.city.str.lower())
             .volume_sold.sum() /
           popn.Population.astype(float)).dropna()
per_cap.plot.barh(figsize=(10, 10), color='k', width=.9);
