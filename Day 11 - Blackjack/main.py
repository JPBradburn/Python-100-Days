import random

print("Welcome to blackjack! ")
print()
cards = {"2":2,
         "3":3,
         "4":4,
         "5":5,
         "6":6,
         "7":7,
         "8":8,
         "9":9,
         "10":10,
         "Jack":10,
         "Queen":10,
         "King":10,
         "Ace":11,
}

playerHand = []
computerHand = []
playerAceCount = 0
computerAceCount = 0
playerHandTotal = 0
computerHandTotal = 0

def generate_cards_player(num):
    global playerHandTotal
    global playerAceCount
    for i in range(num):
        playerHand.append(random.choice(list(cards.items())))
        playerHandTotal = playerHandTotal + playerHand[-1][1]
        if playerHand[-1][0] == "Ace":
            playerAceCount = playerAceCount + 1

def generate_cards_computer(num):
    global computerHandTotal
    global computerAceCount
    for i in range(num):
        computerHand.append(random.choice(list(cards.items())))
        computerHandTotal = computerHandTotal + computerHand[i][1]
        if computerHand[i][0] == "Ace":
            computerAceCount = computerAceCount + 1

def play_a_game():
    global playerHand
    global computerHand
    global playerAceCount
    global computerAceCount
    global playerHandTotal
    global computerHandTotal

    playerHand = []
    computerHand = []
    playerAceCount = 0
    computerAceCount = 0
    playerHandTotal = 0
    computerHandTotal = 0

    generate_cards_player(2)
    generate_cards_computer(2)

    playerHandToPrint=("Your cards: ")
    for i in range(len(playerHand)-1):
        playerHandToPrint=playerHandToPrint+str(playerHand[i][0])+", "
    playerHandToPrint = playerHandToPrint + str(playerHand[-1][0])

    print(playerHandToPrint)
    print(f"\nComputer's first card: {computerHand[0][0]}\n")

    if input("Type 'y' to get another card, or 'n' to pass: ").lower() == "y":
        generate_cards_player(1)

    for i in range(50):
        print()

    playerHandToPrint = ("\nYour final hand: ")
    for i in range(len(playerHand) - 1):
        playerHandToPrint = playerHandToPrint + str(playerHand[i][0]) + ", "
    playerHandToPrint = playerHandToPrint + str(playerHand[-1][0])

    computerHandToPrint = ("\nComputer's final hand: ")
    for i in range(len(computerHand) - 1):
        computerHandToPrint = computerHandToPrint + str(computerHand[i][0]) + ", "
    computerHandToPrint = computerHandToPrint + str(computerHand[-1][0])

    while playerAceCount != 0:
        if playerHandTotal > 21:
            playerHandTotal -= 10
        playerAceCount -= 1

    while computerAceCount != 0:
        if computerHandTotal > 21:
            computerHandTotal -= 10
        computerAceCount -= 1

    print(playerHandToPrint)
    print(computerHandToPrint)
    print()
    print("Your total: " + str(playerHandTotal))
    print("Computer's total: " + str(computerHandTotal))
    print()
    if playerHandTotal == 21:
        if computerHandTotal == 21:
            print("Double Blackjack! Wow! It's a tie.")
        else:
            print("Blackjack! You win!")
    elif computerHandTotal == 21:
        print("Blackjack. You lose. =(")
    elif playerHandTotal > 21:
        if computerHandTotal > 21:
            print("Congrats - You both lost. -_-")
        else:
            print("You lose.")
    elif computerHandTotal > 21:
        print("You win!")
    elif playerHandTotal == computerHandTotal:
        print("It's a tie.")
    elif playerHandTotal > computerHandTotal:
        print("You win!")
    else:
        print("You lose.")
    print()
    if input("Type 'y' to play again ").lower() == "y":
        for i in range(50):
            print()
        play_a_game()

play_a_game()

