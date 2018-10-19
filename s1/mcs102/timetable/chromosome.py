from gene import Gene
from random import shuffle
import copy

class Chromosome:
    def __init__(self, timetables):
        self.genes = []
        self.fitness = 0

        for tt in timetables:
            self.genes.append(Gene(tt))
        #generate random permutation
        shuffle(self.genes)
        

        self.fitness = self.getFitness()

    def getFitness(self):
        return 0

    def crossover(self):
        return copy.copy(self)

    def mutate(self, mutationRate):
        for ele in genes:
            ele.mutate(mutationRate)

