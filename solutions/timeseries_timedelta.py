flights['dep_delay_td'] = pd.to_timedelta(flights['dep_delay'], unit='T')
flights['arr_delay_td'] = pd.to_timedelta(flights['arr_delay'], unit='T')
flights.info()