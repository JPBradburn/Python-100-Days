alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the Caesar Cypher.")

def askTask():
    print()
    task = input("Type \"e\" to encode and \"d\" to decode. ").lower()
    if task == "e":
        encode()
    elif task == "d":
        decode()
    else:
        print("Invalid input.")
        askTask()


def encode():
    try:
        plain_message = input("Type your message: ")
        encoded_message = ""
        for letter in range(len(plain_message)):
            encoded_message = encoded_message + alphabet[alphabet.index(plain_message[letter])]
        shift_amount = int(input("Type the shift key: "))
        encoded_message = ""
        for letter in range(len(plain_message)):
            encoded_message = encoded_message + alphabet[(alphabet.index(plain_message[letter]) + shift_amount) % 26]
        print("Your encoded message is: " + encoded_message)
        askTask()
    except:
        print("Invalid input.")
        encode()

def decode():
    try:
        coded_message = input("Type the coded message: ")
        decoded_message = ""
        for letter in range(len(coded_message)):
            decoded_message = decoded_message + alphabet[(alphabet.index(coded_message[letter]))]
        shift_amount = int(input("Type the shift key: "))
        decoded_message = ""
        for letter in range(len(coded_message)):
            decoded_message = decoded_message + alphabet[(alphabet.index(coded_message[letter]) - shift_amount) % 26]
        print("The original message is: " + decoded_message)
        askTask()
    except:
        print("Invalid input.")
        decode()

askTask()