cols = ['state_bottle_cost', 'state_bottle_retail', 'sale']
df[cols] = df[cols].apply(from_dollars)
