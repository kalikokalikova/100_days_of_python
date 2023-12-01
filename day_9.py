import os

more_bidders = True
bids = {}
winner = ""

while more_bidders:
  bid_name = input("Enter bidder's name: ")
  bid_amount = int(input("Enter bid: $"))
  bids[bid_name] = bid_amount
  os.system("clear")

  keep_going = input("Are there any other bidders? Type 'y' or 'n': ")
  more_bidders = bool(keep_going == 'y')

highest_bid_so_far = 0
for k,v in bids.items():
  if v > highest_bid_so_far:
    highest_bid_so_far = v
    winner = k

print(f"The winner is {winner} with their bid for ${highest_bid_so_far}")


