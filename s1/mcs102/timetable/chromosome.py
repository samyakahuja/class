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
        #for correct averages(otherwise get divide by zero)
        #set initial fitness to 1
        self.fitness = 1
        
        #constraint - 1
        #teacher takes only one class in a slot across all schedules
        nSlots = len(self.genes[0].timetable.slots)
        nConflicts = 0
        #note: '*' in line below is used for unpacking the list
        combIter = list(zip(*[t.timetable.slots for t in self.genes]))
        for i, timeslot in enumerate(combIter):
            #check if all timeslots are not assigned
            if all(v is None for v in timeslot):
                continue
            #check if any one is repeated
            ts_without_none = [x for x in timeslot if x is not None]
            teacherList = [x.subject.teacher.id for x in ts_without_none if x.subject is not None]
            teacherSet = set(teacherList)
            if len(teacherList) == len(teacherSet):
                continue
            else: nConflicts += 1
        self.fitness += nSlots - nConflicts

        #constraint - 2
        #lectures and practicals of a class on "same" day should be together
                


    def crossover(self):
        return copy.copy(self)

    def mutate(self, mutationRate):
        for ele in self.genes:
            ele.mutate(mutationRate)
  
    #TODO
    def output(self):
        print('Printing Schedule')

