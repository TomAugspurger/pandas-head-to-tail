url = 'https://en.wikipedia.org/wiki/List_of_largest_Iowa_cities_by_population'
popn = (pd.read_html(url, header=0)[0]
          .set_index("City")
          .rename(lambda x: x.lower()))
popn.head()
