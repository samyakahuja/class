import random

class Gene:
    def __init__(self, timetable):
        self.timetable = timetable

    def perm(self):
        self.timetable.perm()

    def mutate(self, mutationRate):
        for i in range(len(self.timetable.slots)):
            if random.random() < mutationRate / 2:
                self.timetable.flip(i)
