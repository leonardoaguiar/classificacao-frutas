import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

iris = load_iris()

# print(iris.feature_names)
# print(iris.target_names)
# print(iris.data[0])
# print(iris.target[0])

# 0 = indice da primeira setosa
# 50 = indice da primeira versicolor
# 100 = indice da primeira virginica
test_idx = [0, 50, 100]

# separação dos dados de treino e teste

# dados para treino
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# dados para teste
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

# print(test_target)
# print(clf.predict(test_data))

# visualizar arvore de decisao
# dot_data = StringIO()
# tree.export_graphviz(clf, out_file=dot_data, feature_names=iris.feature_names,
#                      class_names=iris.target_names, filled=True, rounded=True,
#                      impurity=False)

# graph = pydot.graph_from_dot_data(dot_data.getvalue())
# graph[0].write_pdf("iris.pdf")

# visualizar dados de testes
print(test_target[1], test_data[1])
print(iris.feature_names)
print(iris.target_names)
