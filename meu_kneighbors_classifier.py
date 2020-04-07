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
