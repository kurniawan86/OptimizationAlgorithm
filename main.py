from objectivefile import Objective
from psofile import PSO

# ini digunakan untuk running mesin deisel
if __name__ == '__main__':
    nPopulasi = 50
    nDim = 4
    inersia = 1
    maximini = 'min'
    maxloop = 50
    pso = PSO(nPopulasi, nDim, inersia, maximini, maxloop, Function='koefesienDiesel')
    # x = [1,2,3,4]
    # obj = Objective()
    # obj.koefesienDiesel(x)