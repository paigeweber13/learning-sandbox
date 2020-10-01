import numpy
# import tensorflow.keras.datasets.mnist as mnist
from keras.datasets import mnist

def main():
    # fix random seed for reproducibility
    seed = 7
    numpy.random.seed(seed)

    # load data
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # flatten 28*28 images to a 784 vector for each image
    num_pixels = X_train.shape[1] * X_train.shape[2]
    X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32')
    X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32')

    X_train = X_train / 255
    X_test = X_test / 255
