import taxDependencies

taxAmount = int(input("please input your gross yearly income"))

incomeTax = taxDependencies.getIncomeTax(taxAmount)
print(f"Your income tax will be {incomeTax}, leaving your income at {taxAmount - incomeTax}")


        
