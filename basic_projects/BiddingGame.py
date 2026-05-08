
print('''
                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

def highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0
    for bids in bidding_dict:
        bid_amount = bidding_dict[bids]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bids
    print(f"{winner} has the highest bid ${highest_bid}")


bidders = {}
should_continue = True

while should_continue == True:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bidders[name] = bid

    restart = input("Are there any bidders? Type 'yes' or 'no'\n").lower()
    if restart == "no":
        should_continue = False
        highest_bidder(bidders)

