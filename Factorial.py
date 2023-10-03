num = int(input("Enter a number or else"))

newNum = 1
x = 1

while x <= num:
    newNum *= x
    x += 1

print(f"Factorial of {num} = {newNum}")