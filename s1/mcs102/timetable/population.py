from chromosome import Chromosome
import random

class Population:
    def __init__(self, size, cRate = 1e0, mRate = 1e-1, timetables):
        self.size = size
        self.crossoverRate = cRate
        self.mutationRate = mRate
        self.generations = 0
        self.population = []

        for i in range(self.size):
            this.population.append(Chromosome(timetables))
    
    def calcFitness(self):
        for ele in self.population:
            ele.getFitness()

    def generate(self):
        "Create new generation based on current one"

        //normalize fitness of current generation
        sum = 0
        normalized = []
        for ele in self.population:
            sum += self.population
        for ele in self.population):
            normalized.append(ele.fitness / sum)

        new_population = []

        for ele in self.population:
            parent = self.selectParent(normalized)
            child = parent.crossover()
            child.mutate(self.mutationRate)
            new_population.append(child)

        self.population = new_population.copy()
        self.generations += 1

    def selectParent(self, normalized):
        "using simplified rejection sampling procedure"

        index = 0
        r = random.random()

        while r > 0:
            r -= normalized[index]
            index += 1
        index -= 1
        return self.population[index]

    def getAverageFitness(self):
        total = 0
        for ele in self.population:
            total += ele.fitness
        return total / len(self.population)

    def getBest(self):
        pass
