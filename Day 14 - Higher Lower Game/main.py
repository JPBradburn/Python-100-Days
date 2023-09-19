import random

import art
import game_data

print(art.logo)

score = 0


def turn(A):
    global score

    B = random.choice(game_data.data)
    print()
    print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}")
    print(art.vs)
    print(f"Compare B: {B['name']}, a {B['description']} from {B['country']}")
    print()

    if game_data.data.index(eval(input("Who has more followers? Type 'A' or 'B': ").upper())) == min(game_data.data.index(A), game_data.data.index(B)):
        for i in range(50):
            print()
        print(art.logo)
        score += 1
        print("You're right! Current score: " + str(score))
        turn(B)
    else:
        print(art.logo)
        print("Sorry, that's wrong. Final score: " + str(score))
        if input("Do you want to play again? ('Y' / 'N'): ").lower() == "y":
            turn(random.choice(game_data.data))


turn(random.choice(game_data.data))
