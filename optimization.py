from psofile import PSO
from GAfile import GA
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
        elif self.algo == 'GA':
            self.GA_algorithm()

    def GA_algorithm(self):
        nPop = 5
        nDim = 2
        Cr = 0.8
        maxloop = 20
        Mr = 0.2
        obj = GA(nPop, nDim,maxloop, self.obj)
        obj.initPosition()
        # obj.viewPosition()
        obj.calFitness()
        # obj.viewFitness()
        obj.getGbest()
        # print(obj.bestInd)
        # print(obj.bestFitness)
        # print(obj.selec_turnamen())
        # obj.pickParent()
        obj.mainAlgorithm(Cr,Mr)

    def PSO_algorithm(self):
        nPopulasi = 50
        nDim = 2
        inersia = 1
        maximini = 'min'
        maxloop = 100
        PSO(nPopulasi, nDim, inersia, maximini, maxloop, self.obj)