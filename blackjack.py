import random


print ('''
***********************************************
*****************  Blackjack  *****************
***********************************************
''')


class Player:
	def __init__(self):
		self.player_total = 0
		self.name = input("Enter your name: ")
		self.hit = False
		self.cards = []

	def get_card(self):
		pass
	
	def update_player_total(self):
		if not str(self.card).isnumeric():
			Game.convert_faces()
		self.player_total+=int(self.card)
		
class Deck:
	def __init__ (self):
		self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

	def rand_card(self):
		self.card = random.choice(self.deck)
		self.cards.append(self.card)
		return self.card

	def convert_faces(self):
		if card in ["J", "Q", "K"]:
			player.player_total +=10
		elif card == "A":
			self.ace_choice()

class Dealer:
	def __init__(self):
		self.dealer_total = 0

	def rand_card_dealer(self):
		#keeps running until dealer hits 17 or higher
		card = random.choice(self.deck)
		return card

class Turn:
	#turn object should give player options/manage the turn
	#report to game obj, update player obj.
	def __init__(self, player):
		self.deck = Deck()
		self.player = player()
		self.dealer
		self.rand_card()
		self.display_cards()
			#methods below should be part of display_cards() method
			self.calc_total()
			self.display_total()
		self.hit_or_stay()
		#outcome/compare to see if bust
		#dealer hit
		#output

	def display_cards(self):
			#graphical display of cards, figuring out value and giving to user
			card = deck.rand_card()
			player.get_card(card) #get_card should append the card to the self.cards
			total = self.calc_total()
			print(player.cards, total)
			self.hit_or_stay()

	def hit_or_stay(self):
		print("Your total is {}, would you like to hit or stay?".format(self.player_total))

	def calc_total(self):
		pass
		#takes player cards and give it back to player

class Game():
	def __init__(self):
		#turn, dealer, and player should be in here
		pass
		self.setup()
		
	def set_up(self):
		self.player = Player()
		self.turn()
		#dealer has to play here
		self.compare()
		self.results()

	

	def compare(self):
		#compare dealer & player totals
		pass

	def ace_choice(self):
		ace=(input("You have an Ace, please choose 11 or 1"))
		if ace == "1":
			player.player_total +=1
		else:
			player.player_total +=11

	def display_total(self):
		#shows player/dealer totals during/after each game
		pass

	def results(self):
		#player wins, dealer wins
		pass




# g=Game(Player)
# d=Dealer()
p=Player()
p.rand_card_player()







