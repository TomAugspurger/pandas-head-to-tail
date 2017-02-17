def from_dollars(col):
    return pd.to_numeric(col.str.lstrip('$'))
