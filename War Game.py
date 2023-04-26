#you can reference global things like import random, tuples, lists, dictionaries etc
import random
#tuples of all suits and ranks (i dont want to change these)
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#comparing 'print(two_hearts)' to other cards will be impossible because you cannot compare string values.
#so we need to make a dictionary of values assigned to each keyword and compare those instead

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
#the value dictionary will then be an attribute in the class
#using 'rank' instead of self.rank because inside the initiation we are already using rank,
#so the code expects us to pass in a string for the rank value of the card
#however the rank must be written exactly the same as the dictionary keyword otherwise we will get an error
#therefore

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        #^doesn't take user input because all decks should be the same ^
        for suit in suits:
            for rank in ranks:
                #create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            #list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # for a single card object added
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

new_deck = Deck()
new_deck.shuffle()
mycard = new_deck.deal_one()

first_card = new_deck.all_cards[0]
bottom_card = new_deck.all_cards[-1]
#for card_object in new_deck.all_cards:
    #print(card_object)

new_player = Player("Jordan")
new_player.add_cards(mycard)
print(new_player)
new_player.add_cards([mycard, mycard, mycard])
print(new_player)

#Game setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_number = 0

while game_on:
    round_number += 1
    print(f"Round {round_number}")

    if len(player_one.all_cards) == 0:
        print('Player One is out of cards, Player Two wins!')
        game_on = False
        break
        #^the braek line here is kinda pointless since game_on = False will break
        #out of the while loop anyway since it only loops if game_on = True

    if len(player_two.all_cards) == 0:
        print('Player two is out of cards, Player One wins!')
        game_on = False
        break
        #^the braek line here is kinda pointless since game_on = False will break
        #out of the while loop anyway since it only loops if game_on = True

    #start a new round
    player_one_cards = []
    #^'player ones cards' is the cards that the player is using on the table (in play)
    #^vs player one all cards which is the cards that the player has in their hand
    player_one_cards.append(player_one.remove_one())
    for card in player_one_cards:
        print(card)
    #print(player_one_cards)
    #^adds/appends a card to player ones in-play cards, and remove that card from their hand as a consequence

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    for card in player_two_cards:
        print(card)
    #print(player_two_cards)

    #while at war

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
        #using -1 to make sure that we don't keep comparing the first card drawn
        #after 5 more cards are drawn from the initial war trigger, we want to be comparing the 6th card instead
            player_one.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
        #gives player one their cards back, plus player twos cards

            at_war = False

        elif    player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)

                at_war = False
        else:
            print("WARRRRRR!")

            if len(player_one.all_cards) < 10:
                print("Player One cannot go to war")
                print("Player Two Wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < 10:
                print("Player Two cannot go to war")
                print("Player One Wins!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    #essentially calling to remove one card from their hand to place onto the board, 5 times for both

