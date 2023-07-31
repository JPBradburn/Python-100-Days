import random
choicesDict = {
    0 : "rock",
    1 : "paper",
    2 : "scissors"
}
wantToPlay = "p"

def getChoice():
    global userChoice
    userChoice = input("What do you choose? 0 for rock, 1 for paper, 2 for scissors. \n")

while wantToPlay == "p":
    getChoice()
    while userChoice != "1" and userChoice != "2" and userChoice != "0":
        print("Please choose a valid input (0, 1, 2).")
        getChoice()
    print("\nYou chose: " + choicesDict[int(userChoice)] + "\n")
    computerChoice = random.randint(0,2)
    print("Computer chose: " + choicesDict[computerChoice])
    if (computerChoice == int(userChoice)):
        print("It's a tie.")
        print(r'''
        ______
       /(    )\
       \ \  / /
        \/[]\/
          /\
         |  |
         |  |
         |  |
         |  |
         |  |
         \  /
          \/
        ''')
    elif (int(userChoice) == 0 and computerChoice == 1) or (int(userChoice) == 1 and computerChoice == 2) or (int(userChoice) == 2 and computerChoice == 0):
        print("The computer wins. 😭")
    else:
        print("You win! 🥳")

    wantToPlay = input("Press p to play again ")