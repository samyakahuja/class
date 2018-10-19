from gene import Gene
from random import shuffle
import copy

class Chromosome:
    def __init__(self, timetables):
        self.genes = []
        self.fitness = 1

        for tt in timetables:
            temp_gene = Gene(tt)
            temp_gene.perm()
            self.genes.append(temp_gene)

    #TODO
    def calcFitness(self):
        self.fitness = 1

    def crossover(self):
        return copy.copy(self)

    def mutate(self, mutationRate):
        for ele in self.genes:
            ele.mutate(mutationRate)
  
    #TODO
    def output(self):
        print('Printing Schedule')

