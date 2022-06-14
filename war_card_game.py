import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return  self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.all_cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop()

class Player():

    def __init__(self, name):
        self.name = name
        self.all_cards = [] 

    def remove_card(self):
        return self.all_cards.pop(0) 
 
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple card objects
            self.all_cards.extend(new_cards)
            # For a single card object
        else: 
            self.all_cards.append (new_cards)
            
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


player_one = Player("Mong Kong")
player_two = Player("Mong Chick")
min_cards = 7 # Minimum cards required for war

deck = Deck()
deck.shuffle()

for card in range(26):
    player_one.add_cards(deck.deal_card())
    player_two.add_cards(deck.deal_card())

game_on = True
round_number = 0

while game_on:
    round_number += 1
    print(f'Round number: {round_number}')

    # If the war goes into infinite loop, player with more cards win by default.
    if round_number > 5_000:
        print(f'{player_one.name} has won by default') if len(player_one.all_cards) > len(player_two.all_cards) else print(f'{player_two.name} has won by default')
        break

    if len(player_one.all_cards) == 0:
        print(f'{player_one.name} has ran out of cards! {player_two.name} has won!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(f'{player_two.name} has ran out of cards! {player_one.name} has won!')
        game_on = False
        break

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print('WAR!')

            if (len(player_one.all_cards) < min_cards):
                print(f'{player_one.name} is short of cards to continue the war.')
                print(f'{player_two.name} has won!')
                game_on = False
                break

            elif (len(player_two.all_cards) < min_cards):
                print(f'{player_two.name} is short of cards to continue the war.')
                print(f'{player_one.name} has won!')
                game_on = False
                break

            else:
                for num in range(min_cards):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())