import random

possibleMoves = ["Rock","Paper","Scissors"]
player = 0
computer = 0

def CompChoice(moves):
    return moves[random.randint(0,2)]

def getWinner(playerChoice,compChoice):
    possibleWins = ["Draw",["Player wins: Rock beats scissors","Player wins: Paper wraps rock","Player wins: Scissors cut paper"],
                    ["Computer wins: Rock beats scissors","Computer wins: Paper wraps rock","Computer wins: Scissors cut paper"]]
    
    if playerChoice == compChoice:#draw[0]
        return possibleWins[0]
    elif playerChoice == "Rock" and compChoice == "Paper":#computer wins[2]
        return possibleWins[2][1]
    elif playerChoice == "Rock" and compChoice == "Scissors":#player wins[1]
        return possibleWins[1][0]
    elif playerChoice == "Scissors" and compChoice == "Paper":#player wins[1]
        return possibleWins[1][2]
    elif playerChoice == "Scissors" and compChoice == "Rock":#computer wins[2]
        return possibleWins[2][0]
    elif playerChoice == "Paper" and compChoice == "Rock":#player wins[1]
        return possibleWins[1][1]
    elif playerChoice == "Paper" and compChoice == "Scissors":#computer wins[2]
        return possibleWins[2][2]

def updatePlayerScore(currentPlay,playerScore):
    if "Draw" in currentPlay:
        playerScore += 1
    elif "Player" in currentPlay:
        playerScore +=1
    return playerScore

def updateComputerScore(currentPlay,compScore):
    if "Draw" in currentPlay:
        compScore += 1
    elif "Computer" in currentPlay:
        compScore += 1
    return compScore



print "Welcome to rock, paper, scissors. Best out of five !\n"
#First loop to keep playing the game
while True:
    #Second loop up to top score
    while True:
        #Third loop to get the right input from user
        while True:
            getPlayerChoice = raw_input("Choose: rock, paper, scissors \n")
            getPlayerChoice = getPlayerChoice.lower().strip().capitalize()
            if getPlayerChoice.lower().strip().capitalize() == "Rock" or \
                getPlayerChoice.lower().strip().capitalize() == "Paper" or \
                getPlayerChoice.lower().strip().capitalize() == "Scissors":
                break

        getCompChoice = CompChoice(possibleMoves)
        result = getWinner(getPlayerChoice,getCompChoice)
        print result
        player = updatePlayerScore(result,player)
        computer = updateComputerScore(result,computer)
        print "Player: %d, Computer: %d\n" % (player,computer)
        if player == 5 and computer ==  5:
            print "This is a draw!\n"
            break
        elif player == 5:
            print "You win!\n"
            break
        elif computer == 5:
            print "You loose!\n"
            break

                                     
    keepPlay = raw_input("Play again? Y/N\n")
    if keepPlay.lower().startswith("n"):
        print "Thanks for playing! Press any key to quit.\n"
        raw_input()
        break
    else:
        player = 0
        computer = 0
            
    




    
