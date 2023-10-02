min = int(input("player 1, please enter a min value"))
max = int(input("player 2, please enter a max value"))

count = 0

while count < 3:
    guess = int(input("guess a number, player 2"))
    if guess in range (max - min):
        print("player 2 wins")
        break

if count >= 3:
    print("Player 1 wins")
