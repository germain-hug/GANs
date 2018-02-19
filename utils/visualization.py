import matplotlib.pyplot as plt
from utils import z_noise, c_noise
import numpy as np


def plot_large(img):
    """ Custom sized image
    """
    fig1 = plt.figure(figsize = (5,5))
    ax1 = fig1.add_subplot(1,1,1)
    ax1.axes.get_xaxis().set_visible(False)
    ax1.axes.get_yaxis().set_visible(False)
    ax1.imshow(img, cmap='gray')
    plt.show()


def plot_results_DCGAN(G):
    """ Plots 10x10 windows from DCGAN generator
    """
    img = np.zeros((10*28,1))
    for i in range(10):
        col = G.predict(z_noise(10)).reshape(10*28,28)
        img = np.concatenate((img,col), axis=1)
    plot_large(img)

def plot_results_WGAN(G):
    """ Plots 10x10 windows from WGAN generator
    """
    img = np.zeros((10*28,1))
    for i in range(10):
        # Remap from tanh range [-1, 1] to image range [0, 255]
        col = np.multiply(np.add(G.predict(z_noise(10)).reshape(10*28,28), 1.0), 255.0/2.0)
        img = np.concatenate((img,col), axis=1)
    plot_large(img)


def plot_results_InfoGAN(G, c):
    """ Plots 10x10 windows from InfoGAN generator
    """
    img = np.zeros((10*28,1))
    for i in range(10):
        x = np.zeros((10,10))
        x[:,2] = c
        # Convert tanh range [-1; 1] to [0; 255]
        col = np.multiply(np.add(G.predict([noise(10),x]).reshape(10*28,28), 1.0), 255.0/2.0)
        img = np.concatenate((col,img), axis=1)
    plot_large(img)
