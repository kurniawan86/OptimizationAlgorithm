import math
import pandas as panda
import numpy as np

class Rosenbrock2D:
    def fitness(self, x):
        x1 = x[0]
        x2 = x[1]
        temp1 = math.pow(math.pow(x1, 2) - x2, 2)
        temp2 = math.pow(x1-1, 2)
        return 100*temp1-temp2

class Step:
    def fitness(self, x):
        sumof = 0
        for i in range(len(x)):
            sumof = sumof + math.pow((x[i] + 0.5), 2)
        return sumof

class Sphere:
    def fitness(self, x):
        n = len(x)
        tot = 0
        for i in range(n):
            tot = tot + math.pow(x[i],2)
        return tot

class Schwefel:
    def fitness(self, x):
        chromosome = x
        alpha = 418.982887
        fitness = 0
        for i in range(len(chromosome)):
            fitness = fitness - chromosome[i] * math.sin(math.sqrt(math.fabs(chromosome[i])))
        return float(fitness) + alpha * len(chromosome)

class Rastrigin:
    def fitness(self, x):
        tot = 0
        for i in range(len(x)):
            tot += math.pow(x[i],2)-10*math.cos(2*math.pi*x[i])+10
        return tot

class Ackley:
    def fitness(self, x):
        n = len(x)
        res1 = 0
        res2 = 0
        for i in range(n):
            res1 += math.pow(x[i], 2)
            res2 += math.cos(2 * math.pi * x[i])
        res1 = res1 / n
        res2 = res2 / n
        return -20 * math.exp(-20 * res1 - math.exp(res2)) + 20 + math.e

class Griewank:
    def fitness(self, x):
        res1 = 0
        res2 = 0
        for i in range(1,len(x)+1):
            res1 =+ math.pow(x[i-1],2)/4000
            res2 = res2*math.cos(x[i-1]/math.sqrt(i))
        return res1-res2+1