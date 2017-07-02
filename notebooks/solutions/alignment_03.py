res = DataReader(series, start='2000-01-01', data_source="fred")
res = res.rename(columns=dict(zip(series, names)))

fig, ax = plt.subplots(figsize=(12, 8))
res[['quits', 'layoffs']].plot.area(
    color=area_colors, ax=ax)
res[['hires', 'openings']].plot(
    ax=ax, color=line_colors, linewidth=3);
