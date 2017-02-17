from sklearn.neighbors import KDTree

# the result of KDTree.query is a list of index
# *positions*, we'll use id_map to go from
# positions back to airport names
id_map = dict(enumerate(locs.index))

tree = KDTree(locs)

distances, indexes = tree.query(locs.values, k=2)
indexes = indexes[:, 1]
distances = distances[:, 1]
neighbors = pd.Series(indexes, index=locs.index).map(id_map)
neighbors.head()
