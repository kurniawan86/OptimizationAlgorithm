from psofile import PSO
from objectivefile import *

class Optimization:
    algo = None
    obj = None

    def __init__(self, algoritma =None, objFunction=None):
        self.algo = algoritma
        self.__pickFunction(objFunction)
        self.mainMethod()

    def __pickFunction(self, name):
        if name == "Rosenbrock":
            self.obj = Rosenbrock2D()
        elif name == "Step":
            self.obj = Step()
        elif name == "Sphere":
            self.obj = Sphere()
        elif name == "Schwefel":
            self.obj = Schwefel()
        elif name == "Rastrigin":
            self.obj = Rastrigin()
        elif name == "Ackley":
            self.obj = Ackley()
        elif name == "Griewank":
            self.obj = Griewank()

    def mainMethod(self):
        if self.algo == 'PSO':
            self.PSO_algorithm()

    def PSO_algorithm(self):
        nPopulasi = 50
        nDim = 4
        inersia = 1
        maximini = 'min'
        maxloop = 100
        PSO(nPopulasi, nDim, inersia, maximini, maxloop, self.obj)