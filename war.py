"""
This module implements the War card game.

The game involves two players who draw cards from their respective decks.
The player with the higher-ranked card wins the round.
If the cards have the same rank, a "war" occurs,
and additional cards are drawn to determine the winner.

Other links:
https://www.reddit.com/r/learnpython/comments/7ay83p/war_card_game/
https://codereview.stackexchange.com/questions/131174/war-card-game-using-classes
https://gist.github.com/damianesteban/6896120
https://lethain.com/war-card-game-in-python/
https://hectorpefo.github.io/2017-09-13-Card-Wars/
https://www.wimpyprogrammer.com/the-statistics-of-war-the-card-game
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

    while game_on:
        round_num += 1
        print(f"Round {round_num}")

        if len(player_one.all_cards) == 0:
            print("Player Two Wins!")
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print("Player Two Wins!")
            game_on = False
            break

        # remove from deck place to play
        player_one_cards_in_play = []
        player_one_cards_in_play.append(player_one.remove_one())

        player_two_cards_in_play = []
        player_two_cards_in_play.append(player_two.remove_one())

        # compare
        # if no conflict, add to winner all cards
        # if war, deal three more, then one more to compare
        # whoever wins, takes the cards to all cards

        at_war = True

        while at_war:
            if player_one_cards_in_play[-1].value > player_two_cards_in_play[-1].value:
                player_one.add_cards(player_one_cards_in_play)
                player_one.add_cards(player_two_cards_in_play)
                at_war = False
            elif (
                player_one_cards_in_play[-1].value < player_two_cards_in_play[-1].value
            ):
                player_two.add_cards(player_one_cards_in_play)
                player_two.add_cards(player_two_cards_in_play)
                at_war = False
            else:
                print("WAR!")

                if len(player_one.all_cards) < 3:
                    print("Player One unable to declare war")
                    print("Player Two Wins")
                    game_on = False
                    break
                elif len(player_two.all_cards) < 3:
                    print("Player Two unable to declare war")
                    print("Player One Wins")
                    game_on = False
                    break
                else:
                    for num in range(3):
                        player_one_cards_in_play.append(player_one.remove_one())
                        player_two_cards_in_play.append(player_two.remove_one())
