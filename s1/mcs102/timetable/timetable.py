from timeslot import TimeSlot
import random
from random import shuffle

class TimeTable:

    daysPerWeek = 5
    hoursPerDay = 8 #total time from 9:00 to 17:00
    numSlotsPerDay = hoursPerDay // TimeSlot.duration 
    numSlotsPerWeek = numSlotsPerDay * daysPerWeek

    def __init__(self, course):
        assert course is not None
        self.course = course
        self.slots = [TimeSlot(self.course) for _ in range(0,TimeTable.numSlotsPerWeek)]

        #for each subject assign the slots(random)
        curSlot = 0
        for subject in self.course.subjects:
            slotsNeeded = int(subject.theoryHours + subject.practicalHours)
            #TODO: Encorporate duration in slotsNeeded
            assert slotsNeeded < len(self.slots) - curSlot
            for i in range(slotsNeeded):
                self.slots[curSlot + i] = TimeSlot(self.course, subject)
            curSlot += slotsNeeded

    def perm(self):
        shuffle(self.slots)

    def flip(self, i):
        j = i
        while j == i:
            j = random.randint(0, len(self.slots) - 1)
        self.slots[i], self.slots[j] = self.slots[j], self.slots[i]


