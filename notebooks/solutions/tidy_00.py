df['winning_team'] = np.where(
    df.home_points > df.away_points,
    df.home_team,
    df.away_team)

win = pd.melt(df, id_vars='winning_team', value_vars=['away_team', 'home_team'],
              var_name='home_or_away', value_name='team')
win['won'] = win.winning_team == win.team
win_pct = win.groupby(['team', 'home_or_away']).won.mean()
win_pct.head()
