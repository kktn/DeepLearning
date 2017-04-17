import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def neuron1():
    X = np.array([1.0, 0.5])
    W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    B1 = np.array([0.1, 0.2, 0.3])

    print("X.shape is {0}".format(X.shape))
    print("W1.shape is {0}".format(W1.shape))
    print("B1.shape is {0}".format(B1.shape))

    A1 = np.dot(X, W1) + B1
    print("A1 is {0}".format(A1))

    Z1 = sigmoid(A1)
    print("Z1 is {0}".format(Z1))

# Step function
# x = np.arange(-5.0, 5.0, 0.1)
# y = step_function(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1)
# plt.show()

# Sigmoid function
# x = np.arange(-5.0, 5.0, 0.1)
# y = sigmoid(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1)
# plt.show()

# ReLU function
# print(relu(1))

neuron1()