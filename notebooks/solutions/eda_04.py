pd.concat([df.groupby(df.city.str.lower())[['sale', 'volume_sold']].sum(),
           popn.Population], axis=1, join='inner').pipe(sns.pairplot);
