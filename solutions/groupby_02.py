order = df.groupby("profile_name").review_overall.cumcount()
df.groupby(order).review_overall.mean().plot()
