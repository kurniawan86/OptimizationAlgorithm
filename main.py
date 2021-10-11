
from psofile import PSO

if __name__ == '__main__':
    nPopulasi = 100
    nDim = 2
    inersia = 1
    maximini = 'min'
    maxloop = 100
    pso = PSO(nPopulasi, nDim, inersia, maximini, maxloop, Function='Rosenbrock')