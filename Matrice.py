
import numpy as np
import re
import matplotlib.pyplot as plt
from Graph import *

class Matrice(object):
    def __init__(self, data):
        self.K = self.get_K(data) # kilometres
        self.P = self.get_P(data) # prix
        self.size = len(data)
        self.Theta = self.get_theta(0, 0)
        self.graph = Graph(data)
        self.gradient_descent()

    # matrice pour les données kilometres
    def get_K(self, data):
        ret = []
        for line in data:
            ret.append(line[0])
            ret.append(1)
        M = np.array(ret)
        M = M.reshape(len(data), 2)
        return M
    
    # matrice pour les données prix
    def get_P(self, data):
        ret = []
        for line in data:
            ret.append(line[1])
        M = np.array(ret)
        M = M.reshape(len(data), 1)
        return M
    
    # matrice regroupant theta0 et theta1
    def get_theta(self, theta0, theta1):
        M = np.array([theta0, theta1])
        M = M.reshape(2, 1)
        return M

    def model(self):
        return np.dot(self.K, self.Theta)

    def cost(self):
        #return 1/(2*self.size) * np.sum((self.model() - self.P)**2)
        return (np.sum(np.square(self.model() - self.P)) / (2*self.size))

    def gradient(self):
        return 1/self.size * self.K.T.dot(self.model() - self.P)
        #self.graph.show(float(self.Theta[0]), float(self.Theta[1]))
       # return (np.dot(np.transpose(self.K), self.model() - self.P) / self.size)

    def gradient_descent(self):
        for i in range(0, 10):
            #cost_history = np.zeros(10)
            self.Theta = self.Theta - 0.0000000005 * self.gradient() # trouver pourquoi le cout c'est de la merde
            #cost_history[i] = self.cost()
        print("theta final = ",self.Theta)
        print("cout final = ", self.cost())
        #plt.scatter(self.K[:,0], self.P)
        #plt.plot(self.K, self.model())
        #plt.show()


