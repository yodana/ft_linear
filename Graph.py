import matplotlib.pyplot as plt

class Graph(object):
    def __init__(self, data):
        self.x = self.get_x(data)
        self.y = self.get_y(data)
        
    def get_x(self, data):
        ret = []
        for line in data:
            ret.append(line[0])
        return ret

    def get_y(self, data):
        ret = []
        for line in data:
            ret.append(line[1])
        return ret
    
    def show(self, x, model):
        plt.scatter(self.x, self.y)
        plt.plot(x, model)
        plt.show()