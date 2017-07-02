review_length = df.text.str.len()
gr = df.groupby(review_length).review_overall
gr.mean().plot(style='k.')