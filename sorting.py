import random

def randomGenerator(length):

    random.seed(3)
    randomList = []

    for i in range(length):
        randomList.append(random.randint(0, 100000) % 5 * 23)     
    return randomList


print(randomGenerator(100))

