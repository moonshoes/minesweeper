import string
import time
import Minesweeper as ms
import constant


def createGame():
    valid = False
    while not valid:
        try:
            print("Number of rows:")
            rows = int(input())
            print("Number of columns:")
            columns = int(input())
            print("Thank you. How many mines would you like to find?")
            mines = int(input())
            valid = True
        except:
            print("Something went wrong! Please try again. (Hint: make sure your inputs are numbers.")
    return ms.Minesweeper(rows, columns, mines)

def tryAgain():
    print("Would you like to try again? (yes/no)")
    uinput = input()
    while uinput != "yes" and uinput != "no":
        print("I'm sorry, I don't understand. Would you like to try again? (yes/no)")
        uinput = input()
    return uinput

def showCommands():
    print("There are seven commands you can use during the game:")
    print("- help: shows list of commands.")
    print("- show x y: reveals cell at position x, y. If you reveal a mine, the game will end.")
    print("- guess x y: marks the cell at x, y you suspect to be a mine.")
    print("- undo x y: unmarks the cell at x, y previously marked as a suspected mine.")
    print("- restart: restarts the game with a newly generated board.")
    print("- end: ends the game and shows the game board.")
    print("- close: closes the program.")


if __name__ == '__main__':
    print("Hello! Welcome to Minesweeper.")
    print("Before you can begin playing, we would like you to answer a few questions. How big would you like the board to be?")
    
    game = createGame()

    print("Thank you!")
    print("")

    showCommands()
    print("")

    game.printBoard("user")

    userInputString = "start"
    userInput = userInputString.split(" ")

    print("Your timer starts now. Have fun!")
    startTime = time.time()

    while userInput[0] != constant.CLOSE:
        while userInput[0] != constant.CLOSE and userInput[0] != constant.END and userInput[0] != constant.RESTART and not game.isGameOver() and not game.boardIsFilled():
            print("\nWhat would you like to do? (help, show, guess, undo, restart, end, close)")
            userInputString = input().lower()
            userInput = userInputString.split(" ")

            if userInput[0] == constant.SHOW:
                try: 
                    if game.isEmptyCell(int(userInput[1]), int(userInput[2])):
                        game.showCell(int(userInput[1]), int(userInput[2]))
                        game.printBoard("user")
                    else:
                        print("\nCell has already been revealed. Please try again.")
                except:
                    print("\nCommand not available. Please try again.")
            elif userInput[0] == constant.GUESS:
                try:
                    if game.isEmptyCell(int(userInput[1]), int(userInput[2])):
                        game.guessMine(int(userInput[1]), int(userInput[2]))
                        game.printBoard("user")
                    else:
                        print("\nCell has already been revealed. Please try again.")
                except:
                    print("\nCommand not available. Please try again.")
            elif userInput[0] == constant.UNDO:
                try:
                    if game.isGuess(int(userInput[1]), int(userInput[2])):
                        game.undoGuess(int(userInput[1]), int(userInput[2]))
                    else:
                        print("\nUh oh! Looks like the cell you chose wasn't a suspected mine. Please try again.")
                    game.printBoard("user")
                except:
                    print("\nCommand not available. Please try again.")
            elif userInput[0] == constant.HELP:
                showCommands()
            elif userInput[0] != constant.CLOSE and userInput[0] != constant.END and userInput[0] != constant.RESTART:
                print("\nCommand not available. Please try again.")
        
        if game.isGameOver():
            endTime = time.time()
            print("\nUh oh! Looks like you ran into a mine...")
            print("")
            game.printBoard("game")
            print("\nYour game took {} seconds.".format(endTime - startTime))

            userInputString = tryAgain()
            if userInputString == "yes":
                print("\nAlright! Let's generate a new board.")
                game = createGame()
                startTime = time.time()
                game.printBoard("user")
            else:
                userInputString = constant.CLOSE
        elif game.boardIsFilled():
            endTime = time.time()
            print("\nCongratulations! Looks like you beat the game! It took you {} seconds.".format(endTime - startTime))

            userInputString = tryAgain()
            if userInputString == "yes":
                print("\nAlright! Let's generate a new board.")
                game = createGame()
                startTime = time.time()
                game.printBoard("user")
            else:
                userInputString = constant.CLOSE
        elif userInput[0] == constant.RESTART:
            print("\nAlright! Let's generate a new board.")
            game = createGame()
            startTime = time.time()
            game.printBoard("user")
            userInputString = "empty"
        elif userInput[0] == constant.END:
            print("\nHere is your board:")
            game.printBoard("game")
            print("")

            userInputString = tryAgain()
            if userInputString == "yes":
                print("\nAlright! Let's generate a new board.")
                game = createGame()
                startTime = time.time()
                game.printBoard("user")
            else:
                userInputString = constant.CLOSE
        userInput = userInputString.split(" ")


    print("\nThank you for playing. We hope you had fun!")