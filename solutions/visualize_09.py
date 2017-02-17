sns.lmplot("age", "survived", t, hue="sex",
           logistic=True, x_bins=bins,
           palette=pal);
