sns.factorplot("class", "survived", data=t,
               hue="sex", palette=pal).set(ylim=(0, 1));
