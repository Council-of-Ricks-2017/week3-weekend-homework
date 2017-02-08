Game assumes infinite decks- no suits needed, no tracking or shuffling needed.
Game also assumes only you are playing against the dealer (computer). cannot add players
Game does not implement betting at this time
Game does not implement soft 17 for dealer

- game should open with dealer card showing and your two cards with total
		dealer shows: 7
		your hand: 8 A
		your total: 9 or 19

- ask player to hit or stay
	-hit: dispay updated hand and total
		dealer shows: 7
		your hand: 8 A 2
		your total: 10 or 21 (should be smart and display 21, or if over 21 show lower number)
	-stay: dealer's turn

- dealer turn
	-display full dealer hand (with second card) and total
		dealer hit shows new hand and new total
		dealer hand: 7 9
		dealer total: 16
	-must hit until 17 or greater
		display new hand and toal

-behind the scenes
	-deal a random card
	-display cards and total
	-calculate the total
		-takes into account Aces (including double Aces)
		-converts the faces to 10
	-gives result of BUST if player or dealer goes over 21
	-gives result of Blackjack if you get blackjack
	-compares player and dealer totals
	-displays who wins


dealer shows: [7]
your hand: [8] [A]
your total: 9 or 19

hit or stay? hit ---- clear

dealer shows: [7]
your hand: [8] [A] [2]
your total: 11 or 21 

hit or stay? stay  (if stay, lock score as highest if <= 21)
--- clear

dealer's turn

your hand: [8] [A] [2]
your total: 21

dealer hand: [7] [9]
dealer total: 16

dealer hits

--- clear
your hand: [8] [A] [2]
your total: 21

dealer hand: [7] [9] [8]
dealer total: 24
BUST!

you win!





