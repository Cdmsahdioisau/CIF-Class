from random import randint

play = True

while play == True:
    number = randint(1,5)

    guess = int(input("Guess a number between 1 and 5: "))

    if guess == number:
        print(f"yippe! it was {number}")

    elif guess > 5 or guess < 1:
        print("its 1 to 5")

    else:
        print(f"it was {number}, skill issue")

    play = input("guess again? (y/n): ").lower()
    if play == "y":
        play = True
    else:
        play = False


