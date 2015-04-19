# Mini-project #6 - Blackjack

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "test"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class

class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_SIZE[0] * (0.5 + RANKS.index(self.rank)), CARD_SIZE[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_SIZE[0] / 2, pos[1] + CARD_SIZE[1] / 2], CARD_SIZE)
   
# define hand class
class Hand:
    def __init__(self):
        self.list = []
        return self

    def __str__(self):
        str_list = ''
        for i in self.list:
            str_list += i.suit + i.rank + ' '
        return 'Hand contains ' + str_list

    def add_card(self, card):
        self.list.append(card)
        # add a card object to a hand

    def get_value(self):
        temp_value = 0
        for i in self.list:
            temp_value += VALUES.get(i.rank) # get first value, counting Ace as 1
        for i in self.list:
            if (i.rank == 'A') and (temp_value <= 21 - 10):
                temp_value += 10
        return temp_value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        i = 0
        while i < len(self.list):
            pos_i = (pos[0] + CARD_SIZE[0] * i, pos[1])
            self.list[i].draw(canvas, pos_i)
            i += 1
        # draw a hand on the canvas, use the draw method for cards        
      
# define deck class 
class Deck:
    def __init__(self):
        self.cardlist = []
        for suit in SUITS:
            for rank in RANKS:
                self.cardlist.append(Card(suit, rank))
        return self
        # create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cardlist)
        pass    # use random.shuffle()

    def deal_card(self):
        return self.cardlist.pop()
        # deal a card object from the deck
    
    def __str__(self):
        str_list = ''
        for i in self.cardlist:
            str_list += i.suit + i.rank + ' '
        return 'Deck contains ' + str_list
        pass	# return a string representing the deck

player_hand = Hand()
dealer_hand = Hand()
deck = Deck()    

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck 
    
    # your code goes here
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    print 'plarer: ', player_hand
    print 'dealer: ', dealer_hand
    in_play = True

def hit():
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(deck.deal_card())
        print 'plarer: ', player_hand
    if player_hand.get_value() > 21:
        print 'Player busted. Dealer wins', player_hand.get_value()   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if (dealer_hand.get_value() < player_hand.get_value()) or (dealer_hand.get_value() > 21) :
            print 'Player wins'
        else:
            print 'Dealer wins'
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack by Frank', (20, 60), 60, 'black')
    canvas.draw_text(outcome, (40, 120), 30, 'black')
    canvas.draw_text('Dealer', (20, 180), 40, 'black')
    dealer_hand.draw(canvas, [20,200])
    canvas.draw_text('Player', (20, 380), 40, 'black')
    player_hand.draw(canvas, [20,400])  


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric