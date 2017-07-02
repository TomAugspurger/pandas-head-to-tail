m1 = flights.origin == 'ATL'
most_common = flights.loc[m1, 'dest'].value_counts().index[:3]
m2 = flights.dest.isin(most_common)

flights[m1 & m2].head()
