(df.groupby(df.text.str.count('\w'))
   .review_overall
   .mean().plot(style='k.'))
