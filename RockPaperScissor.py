import random

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
cover = '\033[100m'
border = '\033[107m'
purple = '\033[95m'

choice = input((cover + "Do you want to play?  Y/N  "))
win = 0
loss = 0
draw = 0
total = 0

while choice != 'N':
    if choice == 'Y':
        playerOne = input((border + "Rock, Paper, or Scissors?  "))
        choices = ['Rock', 'Paper', 'Scissors']
        num = random.randint(0, 2)
        playerTwo = choices[int(num)]
        if playerOne == playerTwo:
            print((blue + "Draw!"))
            draw += 1
            total += 1
        elif playerOne == "Rock" and playerTwo == "Scissors":
            print((green + "Rock Crushes Scissor, Player One Wins!!!"))
            win += 1
            total += 1
        elif playerOne == "Rock" and playerTwo == "Paper":
            print((red + "Paper Covers Rock, Player Two Wins!!!"))
            loss += 1
            total += 1
        elif playerOne == "Paper" and playerTwo == "Rock":
            print((green + "Paper Covers Rock, Player One Wins!!!"))
            win += 1
            total += 1
        elif playerOne == "Paper" and playerTwo == "Scissors":
            print((red + "Scissors cut Paper, Player Two Wins!!!"))
            loss += 1
            total += 1
        elif playerOne == "Scissors" and playerTwo == "Paper":
            print((green + "Scissors cut Paper, Player One Wins!!!"))
            win += 1
            total += 1
        elif playerOne == "Scissors" and playerTwo == "Rock":
            print((red + "Rock Crushes Scissors, Player Two Wins!!!"))
            loss += 1
            total += 1
        print((green + "Player One:"), playerOne, "VS", (red + "Player Two:"), playerTwo)
        print(green + ("Wins:"), win, (red + ("Losses:")), loss, (blue + "Draws:"), draw, (purple + " Rounds:"), total)
        choice = input((cover + "Do you want to play?  Y/N  "))
    else:
        choice = input((cover + "Do you want to play?  Y/N  "))
