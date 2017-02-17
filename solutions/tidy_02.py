# RPI
df['home_strength'] = df.home_team.map(rpi.rename(mapping)['RPI'])
df['away_strength'] = df.away_team.map(rpi.rename(mapping)['RPI'])
df.head()
