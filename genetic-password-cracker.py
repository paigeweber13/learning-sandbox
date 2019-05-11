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
def computePerfPopulation(population, password):
    populationPerf = {}
    for individual in population:
        populationPerf[individual] = fitness(password, individual)
    return sorted(populationPerf.items(), key = operator.itemgetter(1), reverse=True)

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
    input_password = sys.argv[1]
    current_population = generateFirstPopulation(100, input_password)

    most_fit_guess = ''
    while(most_fit_guess != input_password):
        pass

if __name__ == '__main__':
    main()
