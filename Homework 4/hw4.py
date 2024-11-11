########################################################
#
# CMPSC 441: Homework 4
#
########################################################



student_name = 'John Nguyen'
student_email = 'jnn5163@psu.edu'



########################################################
# Import
########################################################

from hw4_utils import *
import math
import random



# Add your imports here if used






################################################################
# 1. Genetic Algorithm
################################################################


def genetic_algorithm(problem, f_thres, ngen=1000):
    """
    Returns a tuple (i, sol) 
    where
      - i  : number of generations computed
      - sol: best chromosome found
    """
    pass

  

################################################################
# 2. NQueens Problem
################################################################


class NQueensProblem(GeneticProblem):
    def __init__(self, n, g_bases, g_len, m_prob):
        self.n = n
        self.g_bases = g_bases
        self.g_len = g_len
        self.m_prob = m_prob
    
    def init_population(self):
        population = []
        for _ in range(self.n):
            chromasome=[]
            for _ in range(self.g_len):
                randNum = random.choice(self.g_bases)
                chromasome.append(randNum)
            population.append(tuple(chromasome))
        return population

 
    def next_generation(self, population):
        pass

    def mutate(self, chrom):
        randProb = random.random()
        if randProb > self.m_prob:
            return chrom
        else:
            randIndex = random.randint(0, self.g_len-1)
            randNum = random.choice(self.g_bases)
            newChrom = list(chrom)
            newChrom[randIndex] = randNum
            return tuple(newChrom)
    
    def crossover(self, chrom1, chrom2):
        randIndex = random.randint(0, self.g_len-1)
        firstChrom1 = list(chrom1[:randIndex])
        lastChrom2 = list(chrom2[randIndex:])
        return tuple(firstChrom1 + lastChrom2)

    def fitness_fn(self, chrom):
        nonattacking = int(math.factorial(self.g_len)/(2*(math.factorial(self.g_len-2))))

        def conflict(row1, col1, row2, col2):
            return row1 == row2 or col1 == col2 or abs(row1-row2) == abs(col1-col2)
        
        for i in range(self.g_len):
            for j in range(i+1, self.g_len):
                if conflict(i, chrom[i], j , chrom[j]):
                    nonattacking-=1
        return nonattacking
    
    def select(self, m, population):
        probs = []
        sumFitness = 0
        for i in range(len(population)):
            sumFitness += self.fitness_fn(list(population)[i])

        for i in range(len(population)):
            prob = self.fitness_fn(list(population)[i])/sumFitness
            probs.append(prob)

        probDistribution = [sum(probs[:i]) for i in range(1,len(probs)+1)]

        selected = []
        for i in range(m):
            randNum = random.random()
            for i, probSum in enumerate(probDistribution):
                if probSum>=randNum:
                    selected.append(population[i])
                    break
        return selected

    def fittest(self, population, f_thres=None):
        pass




        
################################################################
# 3. Function Optimaization f(x,y) = x sin(4x) + 1.1 y sin(2y)
################################################################


class FunctionProblem(GeneticProblem):
    def __init__(self, n, g_bases, g_len, m_prob):
        pass

    def init_population(self):
        pass

    def next_generation(self, population):
        pass
        
    def mutate(self, chrom):
        pass
        
    def crossover(self, chrom1, chrom2):
        pass
    
    def fitness_fn(self, chrom):
        pass
    
    def select(self, m, population):
        pass

    def fittest(self, population, f_thres=None):
        pass


if __name__ == "__main__":
    p = NQueensProblem(5, range(8), 8, 0.2)
    population = [(4,2,6,4,7,4,3,4),(3,5,5,1,5,0,7,7),(0,4,0,3,4,5,6,6),(5,7,3,1,7,4,5,7),(6,7,5,7,4,7,5,7)]
    print(p.select(2,population))