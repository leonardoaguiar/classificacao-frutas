import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

max_examples = 10000
data = x_train[:max_examples]
labels = y_train[:max_examples]
