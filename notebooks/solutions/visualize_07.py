g = sns.factorplot("class", "survived", data=t,
                   hue="who", palette=pal, col="who",
                   aspect=.5)
g.set(ylim=(0, 1))
g.despine(left=True);
