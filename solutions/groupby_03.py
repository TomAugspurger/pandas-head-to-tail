# Make a barplot of review times by hour
(df.time.dt.hour
   .value_counts()
   .sort_index()
   .plot.bar(rot=0, color='k', width=.8));
