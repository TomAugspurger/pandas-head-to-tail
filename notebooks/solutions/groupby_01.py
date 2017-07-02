(df.groupby('beer_id')
   .review_overall
   .agg(['mean', 'count'])
   .plot.scatter(x='count', y='mean', color='k',
                 marker='.', alpha=.25));
