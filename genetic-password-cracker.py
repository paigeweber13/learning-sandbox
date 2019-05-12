"""
taken from
https://blog.sicara.com/getting-started-genetic-algorithms-python-tutorial-81ffa1dd72f9
as a jumping-off point
"""

import operator
import random
import sys

# how we define fitness
def fitness (password, test_word):
    """
    fitness is number of correct chars divided by the total number of the chars
    in the password
    """
    if len(test_word) != len(password):
        print('words must be equal length!')
        return
    else:
        score = 0
        i = 0
        while i < len(password):
            if password[i] == test_word[i]:
                score += 1
            i += 1
        return score * 100 / len(password)

# creating the first generation
def generateAWord (length):
    i = 0
    result = ""
    while i < length:
        letter = chr(97 + int(26 * random.random()))
        result += letter
        i +=1
    return result

def generateFirstPopulation(sizePopulation, password):
    population = []
    i = 0
    while i < sizePopulation:
        population.append(generateAWord(len(password)))
        i += 1
    return population

# which population members survive?
## sort population by most fit to least fit
def computePerfPopulation(population, password):
    populationPerf = {}
    for individual in population:
        populationPerf[individual] = fitness(password, individual)
    return sorted(populationPerf.items(), key = operator.itemgetter(1), reverse=True)

# select survivors
def selectFromPopulation(populationSorted, best_sample, lucky_few):
    nextGeneration = []
    for i in range(best_sample):
        nextGeneration.append(populationSorted[i][0])
    for i in range(lucky_few):
        nextGeneration.append(random.choice(populationSorted)[0])
    random.shuffle(nextGeneration)
    return nextGeneration

# breeding
def createChild(individual1, individual2):
    child = ""
    for i in range(len(individual1)):
        if (int(100 * random.random()) < 50):
            child += individual1[i]
        else:
            child += individual2[i]
    return child

def createChildren(breeders, number_of_child):
    nextPopulation = []
    for i in range(len(breeders)/2):
        for j in range(number_of_child):
            nextPopulation.append(createChild(breeders[i], breeders[len(breeders) -1 -i]))
    return nextPopulation

# Mutation
def mutateWord(word):
    index_modification = int(random.random() * len(word))
    if (index_modification == 0):
        word = chr(97 + int(26 * random.random())) + word[1:]
    else:
        word = word[:index_modification] + chr(97 + int(26 * random.random())) + word[index_modification+1:]
    return word
    
def mutatePopulation(population, chance_of_mutation):
    for i in range(len(population)):
        if random.random() * 100 < chance_of_mutation:
            population[i] = mutateWord(population[i])
    return population

def main():
    """
    runs until correct password is guessed
    """
    if(len(sys.argv)) < 2:
        print('usage:', sys.argv[0], 'password-to-guess')
    correct_password = sys.argv[1]
    current_population = generateFirstPopulation(100, correct_password)

    most_fit_individual = ''
    generation = 1
    while(most_fit_individual != correct_password):
        sorted_population = computePerfPopulation(current_population,
            correct_password)
        most_fit_individual = sorted_population[0]
        print('Generation:', generation, 'Most fit individual:', 
            most_fit_individual)
        survivors = selectFromPopulation(sorted_population, 35, 15)
        next_population = createChildren(survivors, 4)
        next_population = mutatePopulation(next_population, 50)
        # sorted_population = []
        # for individual in current_population:
        #     sorted_population.append((individual, fitness(correct_password, 
        #         individual)))
        # # sorted population is a tuple of (string, int) where string is the
        # # guessed word and int is the fitness score
        # sorted_population.sort(key=lambda tup: tup[1])
        # most_fit_individual = sorted_population[0][0]
        # print('Generation:', str(generation).zfill(4), 'most fit individual:',
        #     most_fit_individual)

        # generation += 1
        # # so we have 50 survivors, so each couple will produce 4 children.
        # # survivors is just the string.
        # survivors = selectFromPopulation(sorted_population, 35, 15)
        # current_population = []
        # for i in range(len(survivors), 2):
        #     for j in range(4):
        #         parent_1 = survivors[i]
        #         parent_2 = survivors[i+1]
        #         current_population.append(createChild(parent_1, parent_2))
    print('Password has been found!', 'Input password:', correct_password, 
        'Generated password:', most_fit_individual)

if __name__ == '__main__':
    main()
