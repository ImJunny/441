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
    population = problem.init_population()
    best = problem.fittest(population, f_thres)
    if best: return (-1, best)
    for i in range(ngen):
        population = problem.next_generation(population)
        best = problem.fittest(population, f_thres)
        if best: return (i, best)
    best = problem.fittest(population)
    return (ngen, best)

  

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
        selected = self.select(len(population), population)
        newGen = []
        for chrom1 in population:
            #crossover chrom1 with another chrom from self.select for better crossovers
            chrom2 = random.choice(selected)
            tempChrom = self.crossover(chrom1,chrom2)
            tempChrom = self.mutate(tempChrom)
            newGen.append(tempChrom)
        return newGen

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
        sumFitness = sum([self.fitness_fn(chrom) for chrom in population])

        probDistribution = []
        cumulative_sum = 0
        for chrom in population:
            cumulative_sum += self.fitness_fn(chrom) / sumFitness
            probDistribution.append(cumulative_sum)

        selected = []
        for _ in range(m):
            for j, probSum in enumerate(probDistribution):
                if random.random()<=probSum:
                    selected.append(population[j])
                    break
        return selected

    def fittest(self, population, f_thres=None):
        if f_thres is None:
            bestChrom = max(population, key=self.fitness_fn)
            return bestChrom
        elif f_thres:
            bestChrom = max(population, key=self.fitness_fn)
            if (self.fitness_fn(bestChrom)>=f_thres): return bestChrom
            else: return None
        else:
            return None




        
################################################################
# 3. Function Optimaization f(x,y) = x sin(4x) + 1.1 y sin(2y)
################################################################


class FunctionProblem(GeneticProblem):
    def __init__(self, n, g_bases, g_len, m_prob):
        self.n = n
        self.g_bases = g_bases
        self.g_len = g_len
        self.m_prob = m_prob

    def init_population(self):
        chromosomes = []
        for _ in range(self.n):
            randX = random.uniform(0,self.g_bases[0])
            randY = random.uniform(0,self.g_bases[1])
            chromosomes.append((randX, randY))
        return chromosomes

    def next_generation(self, population):
        populationByFitness = sorted(population, key=self.fitness_fn)
        bestChroms = populationByFitness[:math.ceil(len(population)/2)]

        selected = self.select(len(population), population)

        modifiedBestChroms = []
        for i in range(len(population)//2):
            chrom1 = bestChroms[i]
            chrom2 = random.choice(selected)

            tempChrom = self.crossover(chrom1, chrom2)
            tempChrom = self.mutate(tempChrom)
            modifiedBestChroms.append(tempChrom)
        
        newGen = bestChroms + modifiedBestChroms
        return newGen
        
    def mutate(self, chrom):
        p = random.random()
        if p>self.m_prob:
            return chrom
        else:
            randIndex = random.randint(0,len(chrom)-1)
            randF = random.uniform(0, self.g_bases[randIndex])
            tempChrom = list(chrom)
            tempChrom[randIndex] = randF
            return tuple(tempChrom)
        
    def crossover(self, chrom1, chrom2):
        rand = random.randint(0,1)
        alpha = random.random()
        xNew = (1-alpha) * chrom1[0] + alpha * chrom2[0]
        yNew = (1-alpha) * chrom1[1] + alpha * chrom2[1]
        if rand==0:
            return (chrom1[0], yNew)
        else:
            return (xNew, chrom1[1])
    

    def fitness_fn(self, chrom):
        x = chrom[0]
        y = chrom[1]
        return x * math.sin(4*x) + 1.1 * y * math.sin(2*y)
    

    def select(self, m, population):
        probs = []
        n = len(population)
        for k in range(n):
            prob = (self.n-k)/sum(range(1,n+1))
            probs.append(prob)

        probs = sorted(probs)

        distribution = [sum(probs[:i]) for i in range(1, len(probs)+1)]

        selected = []
        for i in range(m):
            randNum = random.random()
            for i, probSum in enumerate(distribution):
                if randNum<=probSum:
                    selected.append(population[i])
                    break
        return selected


    def fittest(self, population, f_thres=None):
        if f_thres is None:
            bestChrom = min(population, key=self.fitness_fn)
            return bestChrom
        elif f_thres:
            bestChrom = min(population, key=self.fitness_fn)
            if (self.fitness_fn(bestChrom)<=f_thres): return bestChrom
            else: return None
        else:
            return None