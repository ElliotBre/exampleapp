while(True):
    error = False
    try:
        print("I could code this so it changes per what you are trying to calculate but I'm lazy :)")
        sideA = float(input("please enter side A length"))
        sideB = float(input("please enter side B length"))
        sideC = float(input("please enter side C length"))
    except ValueError:
        print("Please Enter an int")
        error = True
        continue
    if not error:
        break


print("Print the length of A given B and C")
print("Print the length of B given C and C")
print("Print the length of C given B and A")

while(True):
    error = False
    try:
        option = input("Please choose option A, B, or C").upper()
    except ValueError:
        print("Please enter a string character")
        error = True
        continue
    if not error:
        match option:
            case "A":
                break
            case "B":
                break
            case "C":
                break
            case _:
                continue

match option:
     case "A":
        sideA = ((sideC * sideC) - (sideB * sideB)) ** 0.5 
        print(sideA)
     case "B":
        sideB = ((sideC * sideC) - (sideA * sideA)) ** 0.5
        print(sideB) 
     case "C":
        sideC = ((sideA * sideA) + (sideB * sideB)) ** 0.5
        print(sideC)
        


