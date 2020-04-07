from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets

from scipy.spatial import distance


def euc(a, b):
    return distance.euclidean(a, b)


class MyKNeighborsClassifier():
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_tests):
        predictions = []
        for row in x_tests:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        best_distance = euc(row, self.x_train[0])
        best_index = 0
        for i in range(1, len(self.x_train)):
            dist = euc(row, self.x_train[i])
            if dist < best_distance:
                best_distance = dist
                best_index = i

        return self.y_train[best_index]


iris = datasets.load_iris()

x = iris.data  # dados de entreda para o algoritmo de classificação
y = iris.target  # labels (rotulos) para o algoritmo de classificação

# A variável x são as características (features) que serão
# analisadas pelo algoritmo de classificação.
# Características (features): petal length; petal width; sepal length; sepal width
# print(iris.data)

# A variável y são os rótulos (labels) que esperamos encontrar.
# Rótulos (labels): (0) setosa; (1) versicolor; e (2) virginica
# print(iris.target)

# Divide os dados e labels para treino e teste.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.5)
print("data size: ", x.size)
print("x_train size: ", x_train.size)
print("x_test size: ", x_test.size)
print("y_train size: ", y_train.size)
print("y_test size: ", y_test.size)

# classifier = KNeighborsClassifier()
classifier = MyKNeighborsClassifier()

classifier.fit(x_train, y_train)

predictions = classifier.predict(x_test)

print("acuracia: ", accuracy_score(y_test, predictions))
