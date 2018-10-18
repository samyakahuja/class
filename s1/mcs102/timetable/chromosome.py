from gene import Gene

class Chromosome:
    def __init__(self, timetables, cRate = 1e0, mRate = 1e-1):
        self.genes = []
        self.crossoverRate = cRate
        self.mutationRate = mRate
        self.fitness = 0

        for tt in timetables:
            self.genes.append(Gene(tt))

        self.fitness = Chromosome.getFitness()

    def getFitness():
        return 0

