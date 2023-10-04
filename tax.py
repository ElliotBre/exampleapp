import taxDependencies

flag = False
while flag == False:
     while True:
        try:
            taxAmount = float(input("please input your gross yearly income"))
        except ValueError:
            print("That is not a number, please enter again. ")
            continue
        break
     
     incomeTax = taxDependencies.getIncomeTax(taxAmount)
     print(f"Your income tax will be {incomeTax}, leaving your income at {taxAmount - incomeTax}")

     if(input("Would you like to calculate again? y/n").lower() != "y"):
        flag = True


        
