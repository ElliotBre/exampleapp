num = int(input("Enter a number or else"))

newNum = 1

for x in range(1,num + 1):
    print(x)
    temp = x
    newNum *= temp


print(f"Factorial of {num} = {newNum}")