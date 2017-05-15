
pd.concat([pd.DataFrame(set_, columns=['A', 'B', 'C']) for set_ in records],
          ignore_index=True)