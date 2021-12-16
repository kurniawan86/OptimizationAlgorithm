from optimization import Optimization
from SL_PSOfile import SL_PSO
from GAfile import GA
if __name__ == '__main__':
    # optimal = Optimization(algoritma='PSO',objFunction='Griewank')

    #List algorithm:
    # * PSO

    #List objective Function
    # * Rosenbrock
    # * Step
    # * Sphere
    # * Schwefel
    # * Rastrigin
    # * Ackley
    # * Griewank

    ##testing for every one
    optimal = Optimization(algoritma='GA', objFunction='Rastrigin')
