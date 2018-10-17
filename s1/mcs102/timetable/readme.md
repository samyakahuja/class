# Timetable Scheduling

## Steps

1. Initialize a population with random DNA
1. Generations
    1. Evaluate **Fitness** of each element in the population
    1. Build a **mating pool** from the population based on fitness
    1. **Reproduce** to create a new population
        + Crossover
        + Mutation

## Design Decisions

### DNA

DNA is how we represent all the information for a unit in the
population. It is really a serialization(encoding) of a possible timetable.

### Fitness Function

Fitness fuction can be a set of constraints. Higher the number of 
constraints met, higher the fitness.

Constraints : 

+ A Teacher takes only one class in a unit time-interval
+ A Class has only one lecture/practical in a unit time-interval
+ In same time-interval only 3 theory classes can be scheduled(#gareeblog)
+ In same time-interval only 2 lab classes can be scheduled(#gareeblog)

Optional Constraints:
+ Preferred time of class for Teacher
+ Lecture of same subject for a class should be together.
