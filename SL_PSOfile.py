from particlefile import Particle
class SL_PSO:
    M = 100
    t = 0
    alpha = 0.5
    beta = 0.01
    m = 0
    nSwarm = 0
    swarm = None
    nDim = 0
    e = 0
    bound = None
    P = None

    def __init__(self, nPop, nDim, bound = None):
        self.bound = bound
        self.nSwarm = nPop
        self.nDim = nDim
        self.m = self.__cal_m()
        self.e = self.__cal_e()

    def __cal_m(self):
        n = self.nDim
        return self.M+(n/10)

    def __cal_e(self):
        return self.beta*self.nDim/self.M

    def initPosition(self):
        burung = []
        for i in range(self.nSwarm):
            burung.append(Particle(self.nDim, bound=self.bound))
        self.swarm = burung

    def viewPosition(self):
        for i in range(self.nSwarm):
            print("no :", i, ": ",
                  self.swarm[i].position)