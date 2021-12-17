import random

class entity:
    ndim = 0
    bound = None
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

class GPC:
    nPop = None
    worker = None
    nDim = 0
    bound = None
    function = None
    loop = 0

    def __init__(self, nPop,nDim ,maxIter, Function = None, bound = None):
        print("hello GPC")
        self.loop = maxIter
        self.nPop = nPop
        self.nDim = nDim
        self.function = Function

    def initPosition(self):
        swarm = []
        for i in range(self.nPop):
            swarm.append(entity(self.nDim, bound=self.bound))
        self.worker = swarm

    def viewPosition(self):
        for i in range(self.nPop):
            print("no :", i, ": ", self.worker[i].position)



