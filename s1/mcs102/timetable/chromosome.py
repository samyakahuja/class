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
        nSlotsPerDay = self.genes[0].timetable.numSlotsPerDay
        for gene in self.genes:
            k = 0
            daySlotList = [gene.timetable.slots[i:i+nSlotsPerDay] 
                           for i in range (0,len(gene.timetable.slots),nSlotsPerDay)]
            daySlotList = [[i for i in x if i.subject is not None] for x in daySlotList]
            daySlotSubjectList = [[x.subject.id for x in slot] for slot in daySlotList]
            daySlotSubjectSet = []
            for ele in daySlotSubjectList:
                daySlotSubjectSet.append(set(ele))
            #compute longest running streak for each subject, add that to fitness
            for i, dayList in enumerate(daySlotSubjectList):
                daySet = daySlotSubjectSet[i]
                for slot in daySet:
                    maxAppear = [0]
                    found = False
                    count = 0
                    for j in dayList:
                        if j == slot and found:
                            count += 1
                        elif j == slot and not found:
                            found = True
                            count += 1
                        elif j != slot and found:
                            found = False
                            maxAppear.append(count)
                            count = 0
                        if j == dayList[len(dayList) - 1] and found:
                            maxAppear.append(count)
                    self.fitness += max(maxAppear)



    def crossover(self):
        return copy.copy(self)

    def mutate(self, mutationRate):
        for ele in self.genes:
            ele.mutate(mutationRate)
  
    def output(self):
        print('Printing Schedule')
        print("Fitness achieved = ", self.fitness)
        for gene in self.genes:
            tt_slots = gene.timetable.slots
            print("Timetable for course", tt_slots[0].course.name)
            for i, slot in enumerate(tt_slots):
                if i % gene.timetable.numSlotsPerDay == 0:
                    print("\n")
                if slot.subject is None:
                    print('EMPTY', end = ",")
                else:
                    print(f'{slot.subject.name}-{slot.subject.teacher.name}', end = ",")
            print("\n\n")





        

