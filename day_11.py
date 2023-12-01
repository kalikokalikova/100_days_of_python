import random
import os

deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_cards(number_of_cards):
    cards = []
    for _ in range(number_of_cards):
        cards.append(random.choice(deck))
    return cards

def process_scores(player_hand, dealer_hand):
    # sum both hands
    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)

    # return winner (closest to 21 without going over)
    print("\nYour hand is "+str(player_hand)+" and your score is "+str(player_score))
    print("The dealer's hand is "+str(dealer_hand)+" and their score is "+str(dealer_score)+"\n")

    # winner logic
    if player_score > 21 and dealer_score > 21:
        print("Everyone loses :(")
    elif player_score == dealer_score:
        print("It's a tie")
    elif dealer_score <=21 and player_score <=21:
        winner = "Dealer" if dealer_score > player_score else "You"
        print(f"{winner} is the winner!")
    elif dealer_score > 21 or player_score > 21:
        winner = "Dealer" if dealer_score < 22 else "You"
        print(f"{winner} is the winner!")
    else:
        print("hmmm something else i haven'th thought of")

def is_bust(hand):
    if sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return sum(hand) > 21

def dealer_plays(hand):
    while sum(hand) < 17:
        hand += deal_cards(1)
    return hand

def play_blackjack():
    game_over = False
    # select 2 cards at random for both hands
    player_hand = deal_cards(2)
    dealer_hand = deal_cards(2)

    while not game_over:
        # show player hand, show one card of dealer hand
        print("Your hand is " + str(player_hand))
        print("The dealer's showing card is " + str(dealer_hand[0]))

        # check for busts
        if not is_bust(player_hand):
            # ask if player wants to hit or stand
            hit_or_stand = input("Do you want to hit or stand? ")
            # if hit deal another card to them
            if hit_or_stand == 'hit':
                player_hand += deal_cards(1)
            else:
                dealer_hand = dealer_plays(dealer_hand)
                process_scores(player_hand, dealer_hand)
                game_over = True
        else:
            dealer_hand = dealer_plays(dealer_hand)
            process_scores(player_hand, dealer_hand)
            game_over = True

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system("clear")
  play_blackjack()


