import random
print ('''
***********************************************
*****************  Blackjack  *****************
***********************************************
''')

class Player:
	def __init__(self):
		#contains dealer as well
		self.dealer = False #update to true when it is dealer turn
		# self.turn = Turn()
		self.cards = Cards()
		self.total = 0

	def add_card(self, card):
		return self.cards.add_card(card)

	def display(self):
		self.cards.display()

class Deck:
	def __init__ (self):
		# self.deck = 
		self.cards = Cards()
		self.cards.cardset = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

	def rand_card(self):
		return random.choice(self.cards.cardset)

class Cards: #should be generic for all cards, point is to be modular
#would take the Ace or Face method, but not the values
	def __init__(self):
		self.cardset = []

	def add_card(self, card):
		self.cardset.append(card)

	def display(self):
		print(self.cardset)

class Turn:
	#turn object should give player options/manage the turn
	#report to game obj, update player obj.
	#shouldn't create anything new. it is a "helper class"
	#just a bunch of functionality

	def __init__(self):
		pass
		# self.deck = Deck()
		self.rand_card()
		self.display()

	def display(self):
		pass
		self.player.total = 0
		self.dealer_total = 0
		self.player.cards = []
		self.dealer_cards = []
		



class Game:
	def __init__(self):
		#turn, dealer, and player should be in here
		self.player = Player()
		self.dealer = Player()
		self.deck = Deck()
		self.setup()
		self.hit_or_stay()

	def setup(self):
		#Card card = self.deck.rand_card()
		self.dealer.add_card(self.deck.rand_card()) #dealer gets 1
		self.player.add_card(self.deck.rand_card()) #payer gets 2
		self.player.add_card(self.deck.rand_card())
		#could do for loop for number of cards if it were many more cards

	def display(self):
		#should eventually display total and status if bust
		print("dealer")
		self.dealer.display()

		print("player")
		self.player.display()

	def convert_faces(self):
		pass
		self.value = 0
		self.ace_high = 11
		self.ace_low = 1

		if self.card in ["J", "Q", "K"]:
			self.value +=10
			#should apply to dealer as well
		elif self.card == "A":
			self.ace_low += self.value
			self.ace_high += self.value
			#ace choice should not be a thing, should just show both totals and be smart when player stays/hits.

	def calc_total(self):
		pass
		self.low_value = 0
		self.high_value = 0


	def hit_or_stay(self):
		self.choice = input("Would you like to hit or stay?").lower()
		if self.choice == "hit":
			self.player.add_card(self.deck.rand_card())
			print("player")
			self.player.display()
			return hit_or_stay()
		else:
			#display player total and status

			#switch to Dealer Turn
			self.player.add_card(self.deck.rand_card())
			


blackjack = Game()
blackjack.display()
