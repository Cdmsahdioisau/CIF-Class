import random

health = 100

Sq1 = "player"
Sq2 = "empty"
Sq3 = "empty"
Sq4 = "empty"
Sq5 = "empty"
Sq6 = "empty"
Sq7 = "empty"
Sq8 = "empty"
Sq9 = "empty"

turns = 0
enemyJustSpawned = False

print("Your goal is to survive until the end of the round."
      " Once you survive long enough, go to the middle square for"
      " your escape! Enemies will spawn in random squares, and "
      "you will have to defeat them to survive. Good Luck!")

difficulty = int(input("Difficulty Scale: "))

turnsToWin = int(input("How many turns until escape (inf for forever)?: "))


while turns <= turnsToWin:
      squares = [Sq1, Sq2, Sq3, Sq4, Sq5, Sq6, Sq7, Sq8, Sq9]

      if enemyJustSpawned:
            enemyJustSpawned = False
      else:
            for squareIndex in range(1, len(squares)):
                  if str(squares[squareIndex]).isdigit():
                        if squares[squareIndex - 1] == "empty":
                              squares[squareIndex - 1] = squares[squareIndex]
                              squares[squareIndex] = "empty"
                        elif squares[squareIndex - 1] == "player":
                              health -= 10
                              squares[squareIndex] = "empty"

      Sq1, Sq2, Sq3, Sq4, Sq5, Sq6, Sq7, Sq8, Sq9 = squares

      print("Turn:", turns)
      print("Health:", health)
      print("Map:", Sq1, Sq2, Sq3, Sq4, Sq5, Sq6, Sq7, Sq8, Sq9)

      action = input("What would you like to do? (move, attack, heal, wait): ")

      if action == "move":
            direction = input("Which direction would you like to move? (left, right): ")

            if direction == "left":
                  if Sq1 == "player":
                        print("You can't move left!")
                  elif Sq2 == "player":
                        Sq1, Sq2 = Sq2, Sq1
                  elif Sq3 == "player":
                        Sq2, Sq3 = Sq3, Sq2
                  elif Sq4 == "player":
                        Sq3, Sq4 = Sq4, Sq3
                  elif Sq5 == "player":
                        Sq4, Sq5 = Sq5, Sq4
                  elif Sq6 == "player":
                        Sq5, Sq6 = Sq6, Sq5
                  elif Sq7 == "player":
                        Sq6, Sq7 = Sq7, Sq6
                  elif Sq8 == "player":
                        Sq7, Sq8 = Sq8, Sq7
                  elif Sq9 == "player":
                        Sq8, Sq9 = Sq9, Sq8

            elif direction == "right":
                  if Sq9 == "player":
                        print("You can't move right!")
                  elif Sq8 == "player":
                        Sq8, Sq9 = Sq9, Sq8
                  elif Sq7 == "player":
                        Sq7, Sq8 = Sq8, Sq7
                  elif Sq6 == "player":
                        Sq6, Sq7 = Sq7, Sq6
                  elif Sq5 == "player":
                        Sq5, Sq6 = Sq6, Sq5
                  elif Sq4 == "player":
                        Sq4, Sq5 = Sq5, Sq4
                  elif Sq3 == "player":
                        Sq3, Sq4 = Sq4, Sq3
                  elif Sq2 == "player":
                        Sq2, Sq3 = Sq3, Sq2
                  elif Sq1 == "player":
                        Sq1, Sq2 = Sq2, Sq1

      elif action == "attack":
            if Sq1 == "player" and str(Sq2).isdigit():
                  Sq2 = int(Sq2) - 25
                  if Sq2 <= 0:
                        Sq2 = "empty"
            elif Sq2 == "player" and str(Sq3).isdigit():
                  Sq3 = int(Sq3) - 25
                  if Sq3 <= 0:
                        Sq3 = "empty"
            elif Sq3 == "player" and str(Sq4).isdigit():
                  Sq4 = int(Sq4) - 25
                  if Sq4 <= 0:
                        Sq4 = "empty"
            elif Sq4 == "player" and str(Sq5).isdigit():
                  Sq5 = int(Sq5) - 25
                  if Sq5 <= 0:
                        Sq5 = "empty"
            elif Sq5 == "player" and str(Sq6).isdigit():
                  Sq6 = int(Sq6) - 25
                  if Sq6 <= 0:
                        Sq6 = "empty"
            elif Sq6 == "player" and str(Sq7).isdigit():
                  Sq7 = int(Sq7) - 25
                  if Sq7 <= 0:
                        Sq7 = "empty"
            elif Sq7 == "player" and str(Sq8).isdigit():
                  Sq8 = int(Sq8) - 25
                  if Sq8 <= 0:
                        Sq8 = "empty"
            elif Sq8 == "player" and str(Sq9).isdigit():
                  Sq9 = int(Sq9) - 25
                  if Sq9 <= 0:
                        Sq9 = "empty"
            else:
                  print("Missed Lol")
      elif action == "heal":
            health += 10
            print("healthed!")
            if health > 100:
                  health = 100

                  print("u at max health")

      elif action == "wait":
            print("You wait for a turn...")

      if Sq9 == "empty":
            Sq9 = 9 + difficulty
            enemyJustSpawned = True
      
      turns += 1

      difficulty += 1

      if health <= 0:
            print("You Died!")
            break

      if health > 0 and turns > turnsToWin:
            print("You Survived!")

