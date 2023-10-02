num = int(input("Enter a number or else"))

newNum = 1
x = 1

while x <= num:
    temp = x
    newNum *= temp
    x += 1

print(f"Factorial of {num} = {newNum}")