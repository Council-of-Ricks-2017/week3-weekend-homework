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
		self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
		self.cards = []
		self.card = self.rand_card_player()

	def hit_or_stay(self):
		print("Your total is {}, would you like to hit or stay?".format(self.player_total))

	def rand_card_player(self):
		self.card = random.choice(self.deck)
		self.cards.append(self.card)
		return self.card


	def update_player_total(self):
		if not str(self.card).isnumeric():
			Game.convert_faces()
		self.player_total+=int(self.card)
		

class Dealer:
	def __init__(self):
		self.dealer_total = 0
		self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

	def rand_card_dealer(self):
		#keeps running until dealer hits 17 or higher
		card = random.choice(self.deck)
		return card

class Game(Dealer): #Game is inheriting the Dealer class.
	def __init__(self):
		pass

		# self.players = []
		# self.target_score = target_score
		# self.winner = None
		# self.winners = [] #list to store multiple winners, if more than one user hits the target_score
		# self.round_count = 0
		# self.add_player()
		# self.round()

	def display_cards(self):
		#graphical display of cards
		print(player.cards)

	def compare(self):
		#compare dealer & player totals
		pass

	def calc_total(self):
		pass

	def convert_faces(self):
		if card in ["J", "Q", "K"]:
			player.player_total +=10
		elif card == "A":
			self.player_ace_choice()


	def player_ace_choice(self):
		ace=(input("You have an Ace, please choose 11 or 1"))
		if ace == "1":
			player.player_total +=1
		else:
			player.player_total +=11


	def display_total(self):
		#shows player/dealer totals during/after each game
		print("Player total is: ".format(player.total))

	def results(self):
		#player wins, dealer wins
		pass




# g=Game(Player)
# d=Dealer()
p=Player()
p.rand_card_player()







