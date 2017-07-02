sns.lmplot("age", "survived", t, hue="class",
           logistic=True, x_bins=bins,
           palette=pal);