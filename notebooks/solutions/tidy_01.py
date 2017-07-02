df['home_win'] = df.home_points > df.away_points
df['point_spread'] = df.home_points - df.away_points
df.head()
