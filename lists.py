import sorting

randomList = sorting.randomGenerator(1000)

for i in range(len(randomList)):
    randomList[i] += 1

newList = [x for x in randomList if x < 65 and x >16]

newList.sort

print(f"original list = {randomList} new list = {newList}")

print(f"{len(newList)} fall in the 16 - 65 range of {len(randomList)} original ages")
