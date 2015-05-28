#!/usr/bin/env python

''' 
   A single-deck, single-player Blackjack Game.
   Aces are initially either high or low, specifiable in 
'''

import itertools
import random

class GameEngine(object):

  score_table = {'dealer':0, 'player': 0} 

  def __init__(self,deck,dealer,player):
    self.deck = deck
    self.dealer = dealer
    self.player = player

  def show_all_hands(self,dealer,player):
    player.show_hand()
    dealer.show_hand()

  def decide_winner(self): 
    self.score_table['dealer'] += 1

  def play_round(self):
    dealer.deal_card(player)
    dealer.deal_card(dealer)
    dealer.deal_card(player)
    dealer.deal_card(dealer)
     
    self.show_all_hands(dealer,player)
    dealer.empty_hand()
    player.empty_hand()

    #while not (dealer.over_21 and player.over_21):
    #  pass
      # code here  

  def run(self):
    while deck:
      self.play_round()
      self.decide_winner()
    for p in self.score_table:
      print "{}: {}".format(p, self.score_table[p])

    p_score, d_score = self.score_table['player'], self.score_table['dealer']
    if d_score > p_score:
      print "The Dealer wins with {} points!".format(self.score_table['dealer']) 
    else:
      print "You win with {} points!".format(self.score_table['player']) 
    return True\
      if raw_input("Play_again ?").strip() in ('y','Y','')\
      else False


class Deck(object):
  '''
     Design Decision: The deck is 'dumb', just contains deck data, 
     not interpretation of that data. This means that the card rank 
     doesn't necessarily correlate to a value.
  '''

  suits = ('Spades','Hearts','Diamonds','Clubs')
  rank = ('Ace','King','Queen','Jack') + tuple(range(2,11)) 

  def __init__(self):
    self.deck = [ card
                  for card in itertools.product(self.rank, self.suits)]
    self.played_cards = []


  def __delitem__(self):
    del self.deck[-1]

  def __len__(self):
    return len(self.deck) 
  
  def __repr__(self):
    return '\n'.join('{} of {}'.format(*c) for c in self.deck)

  def __str__(self):
    return '\n'.join('{} of {}'.format(*c) for c in self.deck)

  def __getitem__(self,index):
    return self.deck[index]

  def __setitem__(self,index,value):
    self.deck[index] = value

  def get_deck(self):
    for i in sorted(self.deck, key=lambda x: (x[0],x[1])):
      # note, this lambda achieves the 'Glennsort' 
      print i

class Dealer(object):
  
  def __init__(self,deck,name='Dealer'):
    self.name = name
    self.hand = []
    self.deck = deck
    self.shuffle_deck()
    self.over_21 = False

  def prompt_player(self): 
    return True\
     if raw_input('Do you want another card?').strip() in ('y','Y','')\
     else False

  def empty_hand(self):
    while self.hand:
      self.deck.played_cards.append(self.hand.pop())

  def deal_card(self,player):
    ''' 
       note, this method needs to change to self.deck.pop() 
       but the author doesn't know how to do it at the moment :[
    ''' 
    player.hand.append(self.deck.deck.pop())

  def show_hand(self):
    for card in self.hand:
      print "{}: {} of {}".format(self.name, *card)

  def show_deck(self):
    ''' debugging method '''
    print '\n'.join(card for card in self.deck)
 
  def shuffle_deck(self):
    # shuffle is an in-place method that returns None
    random.shuffle(deck)

class Player(object):

  def __init__(self,name='me'):
    self.name = name
    self.hand = []
    self.over_21 = False

  def show_hand(self): 
    for card in self.hand:
      print "{}: {} of {}".format(self.name, *card)
 
  def empty_hand(self):
    while self.hand:
      deck.played_cards.append(self.hand.pop())
  

  def stand(self):
    ''' forgo receiving another card ''' 
    pass
  
  def split(self):
    ''' swap out high card with one from dealer's deck '''
    pass

  def hit(self):
    ''' gets a new card from dealer '''
    pass 



while True:
  deck = Deck()
  dealer = Dealer(deck)
  player = Player()
  game_engine = GameEngine(deck,dealer,player)

  if not game_engine.run():
    break
