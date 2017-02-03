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

	def hit_or_stay(self):
		print("Your total is {}".format(self.player_total))


class Dealer:
	def __init__(self):
		self.dealer_total = 0
		self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

	def rand_card(self):
		pass
		#keeps running until dealer hits 17 or higher

	def 


class Game:
	def __init__(self):
		pass

	def display_cards(self):
		#graphical display of cards
		self.rand_card()
		pass

	def compare(self):
		#compare dealer & player totals
		pass

	def calc_total(self):
		pass

	def display_total(self):
		#shows player/dealer totals during/after each game
		pass

	def results(self):
		#player wins, dealer wins
		pass












