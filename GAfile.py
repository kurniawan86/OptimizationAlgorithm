import random
class gen:
    __ndim = None
    __bound = None
    position = []
    fitness = 0
    
    def __init__(self, nDim, bound=None):
        self.__ndim = nDim
        self.__bound = bound
        self.__initPosition()

    def __initPositionNoBound(self):
        gen = []
        for i in range(self.__ndim):
            gen.append(random.random())
        return gen

    def __initPositionBound(self):
        gen = []
        mini = self.__bound[0]
        maxi = self.__bound[1]
        for i in range(self.__ndim):
            ind = random.randint(mini, maxi-1)
            gen.append(ind)
        return gen

    def __initPosition(self):
        if self.__bound == None:
            self.position = self.__initPositionNoBound()
        else:
            self.position = self.__initPositionBound()

    def viewPosition(self):
        print(self.__position)

class GA:
    nPop = None
    pop = None
    nDim = 0
    bound = None
    function = None
    bestInd = None
    bestFitness = 0

    def __init__(self, nPop, nDim, Function=None, bound=None):
        self.nPop = nPop
        self.nDim = nDim
        self.bound = bound
        self.function = Function

    def initPosition(self):
        swarm = []
        for i in range(self.nPop):
            swarm.append(gen(self.nDim, bound=self.bound))
        self.pop = swarm

    def viewPosition(self):
        for i in range(self.nPop):
            print("no :", i, ": ",self.pop[i].position)
    
    def calFitness(self):
        for i in range(self.nPop):
            fit = (self.function.fitness(
                self.pop[i].position))
            self.pop[i].fitness = fit
    
    def viewFitness(self):
        for i in range(self.nPop):
            print("fitness : ", self.pop[i].fitness)
            
    def getGbest(self):
        i = self.__findGbestMin()
        self.bestInd = self.pop[i].position
        self.bestFitness = self.pop[i].fitness
    
    def __findGbestMin(self):
        mini = self.pop[0].fitness
        index = 0
        for i in range(self.nPop):
            if mini > self.pop[i].fitness:
                index = i
                mini = self.pop[i].fitness
        return index