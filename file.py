cars = open("cars.csv", "r")

make = []
numbers = []
totals = []

monthlyTotal = 0
grandTotal = 0

for x in cars:
    x = x[:-2] #cuts off \n for each line but is also cutting off last digit of each number in augist category, need to find a way to filter numeric only last two digits string[len(string) - 2:] and isnumeric() seems promising
    y = x.replace(",", "")
    if(y.isnumeric() == True):
        try:
            list = x.split(",")
            i = 0
            newList = []
            while i < len(list):
                if list[i].isdigit():
                    newList.append(int(list[i]))
                i += 1
            numbers.append(newList)
        except ValueError:
            make.append(x)
    else:
        make.append(x)

for i in range(len(numbers)):
    totals.append(sum(numbers[i]))

for i in range(len(make)):
    print(f"sum of annual sale for {make[i]} is {totals[i]}")
for i in range(8):
    monthlyTotal = 0
    for l in range(len(numbers)):
        monthlyTotal += numbers[l][i]
        grandTotal += monthlyTotal
    print(f"Global monthly car sales total for month {i + 1} = {monthlyTotal}")
      
print(f"This means the grand total of car sales equates to {grandTotal}")
    
print(numbers)