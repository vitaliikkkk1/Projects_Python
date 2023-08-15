import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
        'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
        'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


playing = True


class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " " + self.suit


class Deck:

    def __init__(self):
        self.deck = []  # начинаем с пустого списка
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = " "
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "Find cards in the deck: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = [] # ми починаємо з порожнього списку, як і в колоді, якраз в класі класу.
        self.value = 0 # починаємо зі значення 0
        self.aces = 0 # додаємо атрибут, щоб враховувати тузи

    def add_card(self, card):
        # card - from deck
        self.cards.append(card)
        self.value += values[card.rank]

        # Toose
        if card.rank == "Toose":
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


num_zero = 0
num_one = 1

if 0:
    print("TRUE")

test_deck = Deck()
test_deck.shuffle()

test_player = Hand()

pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)
test_player.add_card(test_deck.deal())
print(test_player.value)


class Chips:

    def __init__(self, total=100):

        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips you want to bet?"))

        except:
            print("Sorry, please enter number")

        else:
            if chips.bet > chips.total:
                print("Sorry, not enough chips. Number of chips available: {}". format(
                    chips.total))
            else:
                break


def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # для контроля цикла while

    while True:
        x = input(
            'Take an additional card (hit) or stay card (stand). Enter h or s')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("dealer's hit")
            playing = False

        else:
            print("Enter h or s")
            continue
        break


def show_some(player, dealer):

    print("\nDealer Cards:")
    print(" <map hidden>")
    print('', dealer.cards[1])
    print("\nPlayer Cards:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer Cards:", *dealer.cards, sep='\n ')
    print("Dealer Cards =", dealer.value)
    print("\nPlayer Cards:", *player.cards, sep='\n ')
    print("Player Cards =", player.value)


def player_busts(player, dealer, chips):
    print("Exaggerating the sum of 21 for the player")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player Win")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Player win! Dealer exaggerate")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer win")
    chips.lose_bet()


def push(player, dealer):
    print("Draw")


while True:
    # Write a welcome message
    print('Welcome to the game of Blackjack! Try to get as close to the sum of 21 as possible without exceeding it!\n\
    The dealer draws additional cards until he receives a total of more than 17. An ace counts as 1 or 11.')

    # Create and shuffle a deck of cards, give each Player two cards
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set the number of Player chips
    player_chips = Chips()  # remember default value is 100

    # Ask the Player for his bet
    take_bet(player_chips)

    # Reveal the cards (but leave one and the Dealer's cards hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # remember this is a variable from our hit_or_stand function

        # Ask the Player if he wants to draw an additional card or stay with the current cards
        hit_or_stand(deck, player_hand)

        # Reveal the cards (but leave one and the Dealer's cards hidden)
        show_some(player_hand, dealer_hand)

        # If the Player's cards are over 21, run player_busts() and exit the loop (break)
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If the Player's cards do not exceed 21, go to the Dealer's cards and take additional. cards up to card total >=17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # We perform various options for completing the game
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    # Tell the Player the amount of his chips
    print("\nThe amount of Player's chips is ", player_chips.total)

    # Ask him if he wants to play again
    new_game = input("Do you want to play again? Enter 'y' or 'n': ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
