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


class Deck:
	def __init__ (self):
		self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
		# return self.deck
		# self.player = Player()
		# self.dealer = Dealer()
		# self.dealer_c/rd = None
		# self.turn_count

	# How do we return rand_card to dealer_cards and player_cards?
	# def player_rand_card(self):
	# 	self.player_card = random.choice(self.deck)
	# 	self.player.cards.append(self.player_card)
	# 	return self.player.cards

	# 	# if len(self.player.cards) in [0, 1]:
	# 	# 	self.player.cards.append(self.player_card)
	# 	# 	self.dealer.cards.append(self.dealer_card)

	# def dealer_rand_card(self):
	# 	self.dealer_card = random.choice(self.deck)
	# 	self.dealer.cards.append(self.dealer_card)
	# 	return self.dealer.cards

		# if len(self.player.cards) in [0, 1]:
		# 	self.player.cards.append(self.player_card)
		# 	self.dealer.cards.append(self.dealer_card)


class Dealer:
	def __init__(self):
		self.name = "Dealer"
		self.dealer_total = 0
		self.hit = True #dealer must hit if/until his total is 17 or more
		# self.card = None
		self.cards = []


class Turn:
	#turn object should give player options/manage the turn
	#report to game obj, update player obj.
	# turn_count
	#If turns = 1, 3, 5+.. then = player; else 2, 4, after player 5+ turns = dealer
	#Maybe turn should count turns to track player/dealer turns
	def __init__(self):
		self.hit = None
		self.dealer_card = None
		self.player_card = None
		# self.deck = Deck()
		self.player = Player()
		self.dealer = Dealer()
		self.player_rand_card()
		self.dealer_rand_card()
		# self.set_up()
		# turn_count += 1
		self.display_cards()
		#2 methods below should be part of display_cards() method
			# self.calc_total()
			# self.display_total()

		#Hit or stay should only run after 4 cards dealt
		self.hit_or_stay()
		# self.set_up()

		#outcome/compare to see if bust
		#dealer hit
		#output

	def player_rand_card(self):
		self.player_card = random.choice(Deck())
		self.player.cards.append(self.player_card)
		return self.player.cards

		# if len(self.player.cards) in [0, 1]:
		# 	self.player.cards.append(self.player_card)
		# 	self.dealer.cards.append(self.dealer_card)

	def dealer_rand_card(self):
		self.dealer_card = random.choice(self.deck)
		self.dealer.cards.append(self.dealer_card)
		return self.dealer.cards


	def display_cards(self):
		#graphical display of cards, figuring out value and giving to user
		# card = deck.rand_card()
		# player.get_card(card) #get_card should append the card to the self.cards
		self.dealer.dealer_total = self.calc_dealer_total()
		self.player.player_total = self.calc_player_total()
		print ("\n{}'s Cards:\t".format(self.dealer.name), self.dealer.cards, "\t", self.dealer.dealer_total)
		print ("\n{}'s Cards:\t".format(self.player.name), self.player.cards, "\t", self.player.player_total, "\n")
		# print(player.cards, total)

		#keep this here or in __init__?, need if function to trigger
		# if player_turn == True:
		# 	self.hit_or_stay()

	def hit_or_stay(self):
		self.hit = input("Your total is {}, would you like to hit or stay?".format(self.player.player_total))
		if self.hit == "hit":
			self.rand_card()
			player_turn = True
		else:
			player_turn = False

	def calc_dealer_total(self):
		for card in self.dealer.cards:
			if not str(card).isnumeric():
				card_value = self.game.convert_faces(card)
				self.dealer.player_total += int(card_value)
				return self.dealer.player_total
			else:
				self.dealer.player_total += card
				return self.player.player_total

	def calc_player_total(self):
		for card in self.player.cards:
			if not str(card).isnumeric():
				card_value = self.game.convert_faces(card)
				self.player.player_total += int(card_value)
				return self.player.player_total
			else:
				self.player.player_total += card
				return self.player.player_total


class Game:
	def __init__(self):
		#turn, dealer, and player should be in here
		# self.deck = Deck() #Do i need this here?
		self.turn = Turn()
		self.set_up()

	def set_up(self):
		self.turn
		self.compare()
		self.results()

	def convert_faces(self, card):
		if card in ["J", "Q", "K"]:
			return 10
		elif card == "A":
			return self.ace_choice()

	def compare(self):
		#compare dealer & player totals
		pass

	def ace_choice(self):
		#Add verification
		ace = (input("You have an Ace, please choose 11 or 1"))
		if ace == "1":
			return 1
		else:
			return 11

	def display_total(self):
		#shows player/dealer totals during/after each game
		pass

	def results(self):
		#player wins, dealer wins
		pass




g = Game()
# dlr = Dealer()
# plyr = Player()
# dck = Deck()
# dck.rand_card()





