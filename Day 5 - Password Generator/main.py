import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pword=[]
print("Welcome to the most secure password generator!")
print()
for i in range(int(input("How many letters would you like in your password? "))):
    pword.append(letters[random.randint(0, len(letters)-1)])
for i in range(int(input("How many symbols would you like in your password? "))):
    pword.append(symbols[random.randint(0, len(symbols)-1)])
for i in range(int(input("How many numbers would you like in your password? "))):
    pword.append(numbers[random.randint(0, len(numbers)-1)])
print()
random.shuffle(pword)
print("Your password is: " + "".join(pword))