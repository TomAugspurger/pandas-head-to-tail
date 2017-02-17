m = t.fare.median()

t['fare_'] = np.where(t.fare < m * 3, t.fare, m * 3)
t.head()
