fg = sns.factorplot("adult_male", "survived", data=t,
                    col="class", hue="class", size=6,
                    aspect=.33, palette="BuPu_d")
fg.set(ylim=(0, 1))
fg.despine(left=True);
