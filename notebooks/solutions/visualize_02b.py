sns.violinplot("class", "fare_", data=t, orient="v",
               palette="YlGn")
sns.despine(left=True)
plt.ylim(0);
