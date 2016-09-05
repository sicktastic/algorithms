from sklearn import tree

X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
# prediction = clf.predict([[2., 2.]])
prediction = clf.predict_proba([[2., 2.]])

print(prediction)
