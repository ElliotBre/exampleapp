
while True:
    error = False
    try:
        number1 = int(input("Please enter a number"))
    except ValueError:
        print("Thats not an int!")
        error = True
        continue
    if error == False:
        break



while(True):
    error = False
    try:
        Operator = input("Please enter an operator: + - / *")
    except ValueError:
        print("Thats not a char!")
        error = True
        continue
    if error == False:
        if len(Operator) == 1:
            match Operator:
                case '+':
                    break
                case '-':
                    break
                case '/':
                    break
                case '*':
                    break
                case _:
                    continue
        else:
            continue


while(True):
    error = False
    try:
        number2 = int(input("Please enter a number"))
    except ValueError:
        print("Thats not an int!")
        error = True
        continue
    if error == False:
        break
    
match Operator:
      case '+':
        number1 += number2
        print(f"Answer is {number1}")
      case '-':
        number1 -= number2
        print(f"Answer is {number1}")
      case '/':
        number1 /= number2
        print(f"Answer is {number1}")
      case '*':
        number1 *= number2
        print(f"Answer is {number1}")
      case _:
        print("Error no operator detected")
                    
    

        

            


    




