logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print("Welcome to the secret auction.")

bids_dict={}

def getBid():
    name=input("What is your name? ")
    bid=int(input("What is your bid? "))
    bids_dict[name] = bid
    if input("Is there another bidder? (y/n)? ").lower() == "y":
        for i in range(100):
            print()
        getBid()

getBid()
sorted_bids = sorted(bids_dict.items(), key=lambda x:x[1], reverse=True)
print("The highest bid is: " + str(sorted_bids[0][0]) + " with a bid of " + str("{:,}".format(int(sorted_bids[0][1]))))