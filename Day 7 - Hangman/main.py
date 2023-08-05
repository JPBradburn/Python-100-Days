import art
import word_list
import random

word = random.choice(word_list.word_list)
lives = 6
string = []
guessed = []
for j in word:
    string.append("_")

print(art.logo)
print(art.stages[6])
print(" ".join(string))
def guess(lives, word, string, guessed):
    letter = input("Guess a letter: ")
    x=0
    guessed.append(letter)
    if letter in word:
        for i in word:
            if i == letter:
                string[x] = letter
            x+=1
        print(" ".join(string))
        print(art.stages[lives])
    else:
        print(f"You guessed {letter}, that's not in the word. You lose a life.")
        lives-=1
        print(" ".join(string))
        print(art.stages[lives])
    if "".join(string) == word:
        print("You win!")
    elif lives == 0:
        print("Game Over")
        print("The word was: " + word)
    else:
        print()
        print()
        print()
        print("Previously guessed: " + ", ".join(guessed))
        guess(lives, word, string, guessed)
guess(lives, word, string, guessed)