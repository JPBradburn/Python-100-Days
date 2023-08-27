import random

print("Welcome to the guessing game!")

def game():
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "hard":
        guesses = 5
    else:
        guesses = 10
    number = random.randint(1,100)
    print("I'm thinking of a number from 1-100.")
    for i in range(guesses):
        print(f"You have {guesses} guesses to guess the number.")
        guesses -= 1
        while True:
            try:
                guess = int(input("Make a guess: "))
                while guess > 100 or guess < 1:
                   guess = int(input("Make a guess from 1-100: "))
                break
            except:
                print("Guess a number from 1-100.")

        if guess == number:
            print("You got it! The number was " + str(number))
            return
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")
    print("No guesses left, you lose. \nThe number was " + str(number))

game()
while input("Do you want to play again? (Type 'Yes' / 'No') ").lower() == "yes":
    for i in range(50):
        print()
    game()