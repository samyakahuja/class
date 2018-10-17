from timeslot import TimeSlot

class TimeTable:

    daysPerWeek = 5
    hoursPerDay = 8 #total time from 9:00 to 17:00
    numSlotsPerDay = hoursPerDay // TimeSlot.duration 
    numSlotsPerWeek = numSlotsPerDay * daysPerWeek

    def __init__(self, studentList = None):
        self.slots = [TimeSlot() for _ in range(0,TimeTable.numSlotsPerWeek)]
        #for each student in studentList assign a slot

