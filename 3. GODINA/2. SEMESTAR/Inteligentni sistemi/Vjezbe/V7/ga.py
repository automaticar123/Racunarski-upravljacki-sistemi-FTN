import numpy as np
import random
import matplotlib.pyplot as plt

def criteria(x):
    # Criteria function
    return 3*x[0]**2 + x[1]**4

def generate_individual(borders: list) -> list:
    return [random.uniform(borders[0][0], borders[0][1]),
            random.uniform(borders[1][0], borders[1][1])]

def generate_first_pop(num_indiv: int) -> list:
    return [generate_individual([[-10, 10], [-10, 10]]) for _ in range(num_indiv)]

def find_elites(num_elites: int, population: np.ndarray, fitness: np.ndarray) -> tuple:
    elites = []
    new_indiv = population
    new_fitness = fitness

    for _ in range(num_elites):
        elite = np.argmin(new_fitness)
        new_fitness = np.delete(new_fitness, elite)
        new_indiv = np.delete(new_indiv, elite, 0)
        elites.append(elite)

    return elites, new_indiv, new_fitness

def crossover(individuals: np.ndarray, picks: list) -> tuple:
    # Switching coordinates
    child_one = [individuals[picks[0][0]][0], individuals[picks[1][0]][1]]
    child_two = [individuals[picks[0][0]][1], individuals[picks[1][0]][0]]
    return child_one, child_two

def mutate(children, mutation_perc):
    for i in range(len(children)):
        perc = random.uniform(0, 1)
        if perc < mutation_perc:
            children[i][0] += random.uniform(-1, 1)
            children[i][1] += random.uniform(-1, 1)

def tournament(num_tour: int, individuals: np.ndarray, fitnesses: np.ndarray,
               mutation_perc: int) -> list:
    
    next_generation = []

    while(len(next_generation) < len(individuals)):
        # Pick # individuals and their fitnesses
        picks = []
        while(len(picks) != num_tour):
            new_pick = random.randint(0, len(individuals)-1)
            if new_pick not in picks:
                picks.append([new_pick, fitnesses[new_pick]])

        # Sort by their fitness
        picks.sort(key= lambda x: x[1])

        # Best two are the parents and we generate children
        child_one, child_two = crossover(individuals, picks)

        # Mutate children
        mutate([child_one, child_two], mutation_perc)

        next_generation.append(child_one)
        next_generation.append(child_two)

    return next_generation

def genetic_algorithm(population: np.ndarray, num_indiv: int, num_gener:int,
                      num_elites: int, num_tour: int, mutation_perc: int) -> tuple:
    
    # Used for plotting the fitness of the best individual
    x = []
    y = []

    current_generation = population
    for iter in range(num_gener):
        # Calculate fitnesses of the current population
        fitness = np.array([criteria(current_generation[i]) for i in range(num_indiv)])

        # Find two best individuals
        elites, new_indiv, new_fitness = find_elites(num_elites, current_generation, fitness)

        # Plot the best one
        x.append(iter); y.append(criteria(current_generation[elites[0]]))

        # 3 - tournament selection without elites which returns the new generation
        new_generation = tournament(num_tour, new_indiv, new_fitness, mutation_perc)

        # Elite individuals also go to the next generation
        for elite_index in elites:
            elite = [current_generation[elite_index][0], current_generation[elite_index][1]]
            new_generation.append(elite)

        if(len(new_generation) == 31):
            print("hello world")
        current_generation = new_generation

    # Find the best individuals from the last generation using elites algorithm
    last_fitness = np.array([criteria(current_generation[i]) for i in range(num_indiv)])
    best_indivs, _, _ = find_elites(num_elites, current_generation, last_fitness)

    # Plot the whole evolution
    plt.plot(x, y, '-o')
    plt.xlabel("Iteracije")
    plt.ylabel("Fitness najbolje jedinke")
    plt.show()

    return current_generation, best_indivs, last_fitness
    
# Make the first population and call genetic algorithm

num_indiv = int(input("Number of individuals? : "))
num_gener = int(input("Number of generations? : "))
num_elites = int(input("Number of elites? : "))
num_tour = int(input("If tournament selection, what type? : "))
mutation_perc = float(input("Mutation percentage? : "))

current_generation, best_indivs, best_fitness = genetic_algorithm(population=np.array(generate_first_pop(num_indiv)), 
                                                                  num_indiv=num_indiv, 
                                                                  num_gener=num_gener,
                                                                  num_elites=num_elites,
                                                                  num_tour=num_tour,
                                                                  mutation_perc=mutation_perc)

print("Best individual: {individual}".format(individual=current_generation[best_indivs[0]]))
print("It's fitness: {fitness}".format(fitness=best_fitness[best_indivs[0]]))