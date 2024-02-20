# ROVIC XAVIER A. ALIMAN
# AIZA C. CABALLERO
#
# BSCS-2
# FEBRUARY 15, 2024

deck_of_cards = [
	'King of Clubs (Black)',
	'King of Hearts (Red)',
	'King of Spades (Black)',
	'King of Diamond (Red)',
	'Queen of Clubs (Black)',
	'Queen of Hearts (Red)',
	'Queen of Spades (Black)',
	'Queen of Diamonds (Red)'
]

left = []
right = []


def shuffle_evens(cards, higher_deck, lower_deck):

	for index in range(1,len(cards)+1):

		if index % 2 == 0:
			higher_deck.append(cards[index-1])
		else:
			lower_deck.append(cards[index-1])


print('\nChoose one card from below, then press \'ENTER\' to continue:')
for card in deck_of_cards:
	print(f'- {card}')

input('...')

# Round 1
shuffle_evens(deck_of_cards,right,left)

print('\nDoes the cards below include your card?')
for card in right:
	print(f'- {card}')

while True:
	user_input = input(': ')

	if user_input.lower() == 'yes':
		deck_of_cards = right + left
	elif user_input.lower() == 'no':
		deck_of_cards = left + right
	else:
		print('# \'Yes\' or \'No\' answers only')
		continue
	break


left = []
right = []

# Round 2
shuffle_evens(deck_of_cards,right,left)

print('\nDoes the cards below include your card?')
for card in right:
	print(f'- {card}')

while True:
	user_input = input(': ')

	if user_input.lower() == 'yes':
		deck_of_cards = left + right
	elif user_input.lower() == 'no':
		deck_of_cards = right + left
	else:
		print('# \'Yes\' or \'No\' answers only')
		continue
	break


left = []
right = []

# Round 3
shuffle_evens(deck_of_cards,right,left)

print('\nDoes the cards below include your card?')
for card in right:
	print(f'- {card}')

while True:
	user_input = input(': ')

	if user_input.lower() == 'yes':
		deck_of_cards = right + left
	elif user_input.lower() == 'no':
		deck_of_cards = left + right
	else:
		print('# \'Yes\' or \'No\' answers only')
		continue
	break

left = []
right = []

# Revelation
shuffle_evens(deck_of_cards,right,left)

king_or_queen_determinant = right[0]


new_left = []
new_right = []

left.reverse()

shuffle_evens(left,new_right,new_left)

color_determinant = new_right[0]
suit_determinant = new_left[0]

the_card = new_left[1]

print(f'\nIs this your card? {the_card}')