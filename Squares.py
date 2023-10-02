x = 1

while x <= 100:
    square = x*x
    print(f"Number = {x} Square = {square}")

    if(square > 2000):
        print("2000 limit passed")
        break

    x += 1

    
