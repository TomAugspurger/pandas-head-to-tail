ids = flights.ORIGIN_AIRPORT_ID.value_counts()
ids = ids[ids >= 500].index
ids
