import random
class GH:
    position = []
    fitness = 0
    ndim = 0

    def __init__(self,ndim):
        self.ndim = ndim
        self.__initPositionNoBound()

    def __initPositionNoBound(self):
        gen = []
        for i in range(self.ndim):
            gen.append(random.random())
        return gen

class GOA:
    dim = 0
    popGH = []
    nPop = 0
    def __init__(self,npop,dim):
        self.dim = dim
        self.nPop = npop

    def initPopulation(self):
        gh = []
        for i in range(self.nPop):
            gh.append(GH(self.dim))
        self.popGH = gh

    def viewPosition(self):
        print(self.nPop)
        print(len(self.popGH))
        for i in range(self.nPop):
            print("no :", i, ": ",self.popGH[i].position)