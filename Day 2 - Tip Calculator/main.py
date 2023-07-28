print("Welcome to the tip calculator.")
total=int(input("What was the total bill? "))
people=int(input("How many people should the bill split between? "))
print(f'Each person should pay ${round(total/people, 2)}')