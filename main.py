from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

def refresh():
    clear()
    print(logo)

def add_bidder():
    add_number = 1
    bidder_dict = {}
    auction_start = True
    while auction_start:
        refresh()
        bidder = input("What is your name?\n> ")
        bidding = True
        refresh()
        while bidding:
            try:
                bid = int(
                input("How much do you want to spend?\nYour bid: €"))
                refresh()
            except:
                print("You need a number to proceed")
                refresh()
                continue
            
            check = input(
             f"Really go with €{bid}?\nPress 'N' to revise or any other key to confirm\n > ").lower()
            if check == "n":
                bidding = True
            else:
                bidding = False
        
        if bidder in bidder_dict:
            add_number += 1
            bidder = bidder + "-" + str(add_number)
        bidder_dict[bidder] = bid
        refresh()
        check = input(
         f"Add another bidder?\nPress 'Y' to add or any key to continue\n > ").lower()
        if check == "y":
            auction_start = True
        else:
            auction_start = False

    return bidder_dict

def auction_winner(auction_list):
    winner = ""
    highest_bid = 0

    for bidder in auction_list:        
       if auction_list[bidder] > highest_bid:
          highest_bid = auction_list[bidder]
          winner = bidder
    refresh()
    print(
     f"The winner of this auction is {winner} with €{highest_bid}")

refresh()
player = add_bidder()
refresh()
auction_winner(player)