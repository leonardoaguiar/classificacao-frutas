from sklearn import tree

solida = 1
macia = 0
laranja = 1
maca = 0

features = [[150, solida], [170, solida], [140, macia], [130, macia]]
labels = ["laranja", "laranja", "maçã", "maçã"]

clf = tree.DecisionTreeClassifier()
trained = clf.fit(features, labels)

print(clf.predict([[130, macia]]))
