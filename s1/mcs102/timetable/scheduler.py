## main file - import logic + AI

import argparse
import os
import csv
import pandas as pd
import re
import sys
import warnings

from teacher import Teacher
from subject import Subject
from course import Course
from timetable import TimeTable
from population import Population


def get_data():
    parser = argparse.ArgumentParser(description = 'TimeTable Scheduler')
    parser.add_argument('path', default = "", help = 'Absolute path to the file')
    parser.add_argument('-v', '--verbose', action = 'count', help = 'increase output verbosity')
    args = parser.parse_args()

    path = args.path
    if not os.path.isfile(path):
        print("Not a valid file path!")
        exit(1)
    fileName, fileExtension = os.path.splitext(path)
    if not fileName or fileExtension != ".csv":
        print(os.path.basename(path), "is not a csv")
        exit(1)

    df = pd.read_csv(path)
    if args.verbose: print("\n\033[0;34mDataframe: \033[0m\n\n",df)

    ##initialize teachers

    teachers = df['teacher'].unique()
    for i, teacher in enumerate(teachers):
        teachers[i] = Teacher(i, teacher)

    if args.verbose:
        print("\n\033[0;34mTeachers: \033[0m\n")
        for teacher in teachers:
            print(teacher.id, teacher.name, teacher)


    ##initialize subjects

    subjects = df['subject']
    for i, row in enumerate(df.values):
        teacher = None
        for t in teachers:
            if t.name == row[1]:
                teacher = t
                break
        tHours = row[2]
        pHours = row[3]
        subjects[i] = Subject(i, row[0], teacher, tHours, pHours)
        #TODO: fix warning - (enable warning at end of code)

    if args.verbose:
        print("\n\033[0;34mSubjects: \033[0m\n")
        for subject in subjects:
            print(subject.id, subject.name, subject.teacher.name,
                    subject.theoryHours, subject.practicalHours)

    
    ##initialize course

    #TODO : dynamically calculate unique_courses
    unique_courses = ['MCA-1','MCA-3','MCS-1','MCS-3']
    courses = []
    for i, course in enumerate(unique_courses):
        regex = r'^' + re.escape(course)
        temp_subs = [subject for subject in subjects if re.match(regex, subject.name)]
        courses.append(Course(i, course, temp_subs))

    if args.verbose:
        print("\n\033[0;34mCourses: \033[0m\n")
        for course in courses:
            print(course.id, course.name, [subject.name for subject in course.subjects])
    

    ##initialize timetables
    timetables = []
    for course in courses:
        timetables.append(TimeTable(course))

    if args.verbose:
        print("\n\033[0;34mTimetables: \033[0m\n")
        for timetable in timetables:
            print(timetable.course.name, [slot.subject.name \
                  for slot in timetable.slots if slot.subject is not None] + 
                  [slot.subject for slot in timetable.slots if slot.subject is None])

    
    return teachers, subjects, unique_courses, courses, timetables



def initialize():
    teachers, subjects, unique_courses, courses, timetables = get_data()
    
    #genetic algo parameter
    populationSize = 100
    generations = 1000
    mutationRate = 1e-1
    best_chromosome = []

    #apply genetic algorithm
    tt_population = Population(populationSize, timetables, mutationRate)
    for _ in range(generations):
        tt_population.calcFitness()
        best_chromosome.append(tt_population.getBest())
        tt_population.generate()
   
    #best over all generations
    overallBest = best_chromosome[0]
    for ele in best_chromosome:
        if ele.fitness > overallBest.fitness:
            overallBest = ele

    overallBest.output()


if __name__ == "__main__":
    #ignore warnings : can be turned back on with python -W
    if not sys.warnoptions:
        warnings.simplefilter("ignore")
    initialize()

