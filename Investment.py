years = 0
investment = int(input("Enter your initial investment."))
interest = int(input("Enter your interest rate"))
target = int(input("Enter your target sum"))

interest = 1 + (interest / 100)

print(interest)

while investment < target:
    print(investment)
    investment *= interest
    years += 1

print(years)