total = 0
for i in 3:
    total += int(input(f"enter number {i}"))

average = total / 3

if average < 65:
    print("Fail")
else:
    print("Pass")

