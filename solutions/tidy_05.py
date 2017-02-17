def compute_away_streaks(v):
    streaks = []
    current_streak = 0

    for row in v:
        if row == 'away_team':
            current_streak += 1
        else:
            current_streak = 0
        streaks.append(current_streak)
    return pd.Series(streaks, index=v.index)