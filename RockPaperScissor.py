import random

choice = input("Do you want to play?  Y/N  ")
win = 0
loss = 0
draw = 0
total = 0

while choice != 'N':
    if choice == 'Y':
        playerOne = input("Rock, Paper, or Scissors?  ")
        choices = ['Rock', 'Paper', 'Scissors']
        num = random.randint(0, 2)
        playerTwo = choices[int(num)]
        if playerOne == playerTwo:
            print("Draw!")
            draw += 1
            total += 1
        elif playerOne == "Rock" and playerTwo == "Scissors":
            print("Rock Crushes Scissor, Player One Wins!!!")
            win += 1
            total += 1
        elif playerOne == "Rock" and playerTwo == "Paper":
            print("Paper Covers Rock, Player Two Wins!!!")
            loss += 1
            total += 1
        elif playerOne == "Paper" and playerTwo == "Rock":
            print("Paper Covers Rock, Player One Wins!!!")
            win += 1
            total += 1
        elif playerOne == "Paper" and playerTwo == "Scissors":
            print("Scissors cut Paper, Player Two Wins!!!")
            loss += 1
            total += 1
        elif playerOne == "Scissors" and playerTwo == "Paper":
            print("Scissors cut Paper, Player One Wins!!!")
            win += 1
            total += 1
        elif playerOne == "Scissors" and playerTwo == "Rock":
            print("Rock Crushes Scissors, Player Two Wins!!!")
            loss += 1
            total += 1
        print("Player One:", playerOne, "VS", "Player Two:", playerTwo)
        print("Wins:", win, "Losses:", loss, "Draws:", draw, " Rounds:", total)
        choice = input("Do you want to play?  Y/N  ")
    else:
        choice = input("Do you want to play?  Y/N  ")

