from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]]

# 0 fo Apple, 1 for Orange
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels) # find patterns and data

print clf.predict([[150, 0]])
