fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='rest_spread', y='home_win',
            data=df.loc[(-3 <= df.rest_spread) &
                        (df.rest_spread <= 3)],
            color='#4c72b0', ax=ax)
sns.despine()