from particlefile import Particle
from psofile import PSO

if __name__ == '__main__':
    pso = PSO(10, 2, bound=[0, 9])
    pso.viewPosition()
    pso.viewFitness()