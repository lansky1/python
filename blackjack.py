import random

SUITES = ("Hearts", "Diamonds", "Spades", "Clubs")
RANKS = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
VALUES = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


class Card:
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return self.rank + " of " + self.suite


class Deck:
    def __init__(self):
        self.all_cards = []
        self.all_cards.extend([Card(suite, rank) for suite in SUITES for rank in RANKS])

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop(0)


class Player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank

    def win_round(self, bet):
        self.bank += bet

    def go_bust(self, bet):
        self.bank -= bet


def show_table(player_cards, dealer_cards, reveal_dealer=False):
    player_sum = sum(card.value for card in player_cards)
    dealer_sum = sum(card.value for card in dealer_cards)

    print("\nYour hand:")
    for card in player_cards:
        print(card)
    print(f"Your total: {player_sum}")

    print("\nDealer's hand:")
    print(dealer_cards[0])

    if reveal_dealer:
        for card in dealer_cards[1:]:
            print(card)
        print(f"Dealer total: {dealer_sum}")
    else:
        print("Hidden card")
        print(f"Dealer showing: {dealer_cards[0].value}")
    print()


if __name__ == "__main__":
    player = Player("Player", 100)

    print(f"The table is open. Welcome to Blackjack, {player.name}.")

    # Dealer plays (17 condition), ace being one condition
    # Decide winner
    # Update money
    # Ask for new bet amount, or quit

    playing = True

    while playing:
        # Prepare the deck
        deck = Deck()
        deck.shuffle()

        print(f"You have ${player.bank} in chips.")

        # Ask Player for a bet amount
        wager_accepted = False
        while not wager_accepted:
            try:
                round_bet = int(input(f"{player.name}, slide your chips forward: "))
            except ValueError:
                print("The dealer raises an eyebrow. That's not a valid wager.")
            else:
                if round_bet <= player.bank:
                    wager_accepted = True
                else:
                    print(
                        "The dealer taps the table. You don't have enough chips for that wager."
                    )

        # Deal 2 Cards to Each
        print("The dealer shuffles the deck and deals the opening hands.")

        player_cards = []
        dealer_cards = []

        player_cards = [deck.deal(), deck.deal()]
        dealer_cards = [deck.deal(), deck.deal()]

        show_table(player_cards, dealer_cards, False)
        # player_sum = sum(card.value for card in player_cards)
        # dealer_sum = sum(card.value for card in dealer_cards)

        # Player plays
        player_turn = True
        while player_turn:
            try:
                player_choice = input(f"{player.name}, hit or stand? ").lower()
            except:
                print("The dealer waits. Call it clearly: hit or stand.")
            else:
                if player_choice == "hit":
                    new_card = deck.deal()
                    player_cards.append(new_card)
                    print(f"The dealer slides you the {new_card}.")
                    show_table(player_cards, dealer_cards, False)
                    player_sum = sum(card.value for card in player_cards)

                    if player_sum > 21:
                        print("You went over 21. The table takes the round.")
                        player.go_bust(round_bet)
                        player_turn = False

                elif player_choice == "stand":
                    player_sum = sum(card.value for card in player_cards)
                    print(f"You hold your hand at {player_sum}.")
                    player_turn = False

                else:
                    print("The dealer taps the felt. Choose 'hit' or 'stand'.")

        if player.bank == 0:
            print("The dealer gathers the last of your chips. You're out of money.")
            playing = False
