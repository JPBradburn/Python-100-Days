while True:
    operation=input("Enter a calculation: ")
    try:
        print('%1g' % eval(operation.replace("x","*")))
    except:
        print("Please enter a valid calculation.")
    print()