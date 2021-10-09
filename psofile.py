from particlefile import Particle
from objectivefile import Objective

class PSO:
    nSwarm = 0
    swarm = None
    obj = Objective()
    fit = []
    gbest = []

    def __init__(self, nPop, nDim, bound=None):
        self.nSwarm = nPop
        self.initPosition(nDim, bound=bound)
        self.calculateFitness()

    def initPosition(self, ndim, bound=None):
        swarm = []
        for i in range(self.nSwarm):
            swarm.append(Particle(ndim, bound=bound))
        self.swarm = swarm

    def viewPosition(self):
        for i in range(self.nSwarm):
            print("no :", i, ": ",
                  self.swarm[i].position)

    def viewFitness(self):
        for i in range(self.nSwarm):
            print("fitness :", i, ": ",
                  self.swarm[i].fitness)

    def calculateFitness(self):
        for i in range(self.nSwarm):
            fit = (self.obj.Rosenbrock2D(
                self.swarm[i].position))
            self.swarm[i].fitness = fit