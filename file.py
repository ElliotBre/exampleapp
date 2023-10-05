cars = open("cars.csv", "r")

make = []
numbers = []
totals = []

monthlyTotal = 0
grandTotal = 0

for x in cars:

    temp = x[len(x) - 2: - 1]
    x = x[:-2] 

    for i in range(len(temp)):
        if(temp[i].isdigit() == True):
            x += temp[i]

    y = x.replace(",", "")

    if(y.isnumeric() == True):
        try:
            i = 0
            newList = []
            list = x.split(",")

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

print("\n")

for i in range(len(make)):
    print(f"Sum of annual sale for {make[i]} = {totals[i]}")

print("\n")

for i in range(8):
    monthlyTotal = 0
    for l in range(len(numbers)):
        monthlyTotal += numbers[l][i]
        grandTotal += monthlyTotal
    print(f"Global monthly car sales total for month {i + 1} = {monthlyTotal}")
      
print(f"\n\nThis means the grand total of car sales equates to {grandTotal}\n")
    