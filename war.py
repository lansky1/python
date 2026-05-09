"""
This module implements the War card game.

The game involves two players who draw cards from their respective decks.
The player with the higher-ranked card wins the round.
If the cards have the same rank, a "war" occurs,
and additional cards are drawn to determine the winner.
"""

import random

suites = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
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
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}


class Card:
    """
    Represents a single playing card with a suit and rank.
    """

    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suite


class Deck:
    def __init__(self):
        self.all_cards = []
        # Composition "has-a" relationship
        # Each Card object is created independently and added to the Deck.
        for suite in suites:
            for rank in ranks:
                created_card = Card(suite, rank)
                self.all_cards.append(created_card)

        # This is wrong, since you cannot do assignment inside a list comprehension
        # self.all_cards.append(created_card = Card(suite,rank)) for suite in suites for rank in ranks]

        # This is the correct way
        # self.all_cards.extend([Card(suite, rank) for suite in suites for rank in ranks])

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop(0)


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # if type(new_cards) == type([]):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"
    
if __name__ == "__main__":
    player_one = Player("P1")
    player_two = Player("P2")
    
    new_deck = Deck()
    new_deck.shuffle()
    
    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())
        
    game_on = True
    round_num = 0
