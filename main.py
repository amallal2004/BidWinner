import os
import art

# Initialize an empty list to store the bids
bid_list = []
# Control variable for the bidding process
end_bid = False
# Print the ASCII art logo
print(art.logo)


# Function to add a bid to the bid_list
def add_bid(bidder, amount):
    """
        Function to add a bid to the bid_list.
        Args:
            bidder (str): The name of the bidder.
            amount (int): The bid amount.
    """
    new_dic = {
        "name": bidder,
        "amount": amount,
    }
    bid_list.append(new_dic)


# Function to determine and display the winner
def result():
    """
       Function to determine and display the winner.
    """
    winner = ""
    win_amount = 0
    for dic in bid_list:
        if win_amount < dic["amount"]:
            win_amount = dic["amount"]
            winner = dic["name"]
    print(f"The winner is {winner} with a bid amount of ${win_amount}")


# Bidding process loop
while not end_bid:
    # Prompt user for their name
    name = input("What's your name?: ")
    # Prompt user for their bid amount
    bid_amount = int(input("What's you bid?: $"))
    # Add the bid to the bid_list
    add_bid(name, bid_amount)
    # Ask if there are any other bidders
    direction = input("Are there any other bidders? Type 'yes or 'no': ").lower()
    # Clear the screen for the next bidder
    os.system('clear' if os.name != 'nt' else 'cls')
    # If there are no more bidders, determine the winner and end the bidding process
    if direction == 'no':
        result()
        end_bid = True

