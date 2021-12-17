from psofile import PSO
from GAfile import GA
from GOAfile import GOA
from GPCfile import GPC
from objectivefile import *

class Optimization:
    algo = None
    obj = None
    fitness = None

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
        elif self.algo == "GOA":
            self.GOA()
        elif self.algo == "GPC":
            self.GPC()

    def GA_algorithm(self):
        nPop = 5
        nDim = 2
        Cr = 0.8
        maxloop = 20
        Mr = 0.2
        obj = GA(nPop, nDim,maxloop, Cr,Mr, self.obj)
        self.fitness = obj.fitness

    def PSO_algorithm(self):
        nPopulasi = 5
        nDim = 2
        inersia = 1
        maximini = 'min'
        maxloop = 20
        PSO(nPopulasi, nDim, inersia, maximini, maxloop, self.obj)

    def GOA(self):
        nPopulasi = 5
        cMax = 1
        cMin = 0.00004
        nDim = 2
        obj = GOA(nPopulasi,nDim)
        obj.initPopulation()
        obj.viewPosition()

    def GPC(self):
        nPopulasi = 10
        maxloop = 2
        ndim = 2
        obj = GPC(nPopulasi, ndim, maxloop, self.obj)
        obj.initPosition()
        obj.viewPosition()
