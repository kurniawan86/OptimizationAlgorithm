import math

class Objective:
    def __init__(self):
        pass

    def Rosenbrock2D(self, x):
        x1 = x[0]
        x2 = x[1]
        temp1 = math.pow(math.pow(x1, 2) - x2, 2)
        temp2 = math.pow(x1-1, 2)
        return 100*temp1-temp2