# Import Stuff
from random import randint

# List to fake weighted RNG
randomNumber = [3,3,2,2,2,1,1,1,1,1,]

# Start Variables
lives = 10

money = 0

roundNumber = 1

averageWage = 0

# Info
print("Choose to number from 1 - 3 to get money\n" \
"1 - 50% - $1\n" \
"2 - 30% - $2\n" \
"3 - 20% - $3\n" \
"You can buy lives using money\n" \
"You have 10 lives, try not to guess wrong." )

# Guess Loop
while lives > 0:
    # Which Number to Gamble On
    guess = int(input("Choose a number from 1 to 3: "))

    # Choose Random Number
    number = randomNumber[randint(0, 9)]

    # Logic
    if guess == number:
        if guess == 3 and guess == number:
            money += 3

            print("You get $3")

        elif guess == 2 and guess == number:
            money += 2
            
            print("You get $2")

        elif guess == 1 and guess == number:
            money += 1

            print("You get $1")

    else:
        print("You lose a life")
        lives -= 1

    # Tell User What They Have
    print(f"You have ${money}")
    print(f"You have {lives} lives")

    # Buy lives
    shop = int(input("Buy Stuff?\n" \
    "1) 1 life - $3\n" \
    "2) 3 lives - $5\n" \
    "3) Nope\n"
    "Choose which option (type its number): "))

    if shop == 1:
        if money == 3:
            lives += 1

            print("Bought")
        else:
            print("Not enough money, need $3")

    elif shop == 2:
        if money == 5:
            lives += 3

            print("Bought")
        else:
            print("Not enough money, need $5")

    elif shop == 3:
        print("bye")

    roundNumber += 1

print("You Lost :(")
print(f"You got ${money} and survived {roundNumber} rounds")
averageWage = str(money / roundNumber)
print(f"You got around ${averageWage} per round")