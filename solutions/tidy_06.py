# fill 1 for teams that start on the road
away_streaks = (
    tidy.groupby("team")
        .variable
        .transform(compute_away_streaks).fillna(1))
away_streaks.head()
