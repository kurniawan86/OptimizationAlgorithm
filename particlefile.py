import random
class Particle:
    position = []
    fitness = []
    pbest = []
    velocity = []
    ndim = 0
    bound = None

    def __init__(self, ndim, bound=None):
        self.ndim = ndim
        self.bound = bound
        self.__initPosition()

    def __initPositionNoBound(self):
        gen = []
        for i in range(self.ndim):
            gen.append(random.random())
        return gen

    def __initPositionBound(self):
        gen = []
        mini = self.bound[0]
        maxi = self.bound[1]
        for i in range(self.ndim):
            ind = random.randint(mini, maxi-1)
            gen.append(ind)
        return gen

    def __initPosition(self):
        if self.bound==None:
            self.position = self.__initPositionNoBound()
        else:
            self.position = self.__initPositionBound()



