import random
from src.estate import *
from src.player import *


class Board:

    FIRST_POSITION = 0

    def __init__(
        self,
        estates=None,
        estate_quantity=20,
        full_round_value=100,
        estate_buy_cost_min=100,
        estate_buy_cost_max=1000,
        estate_rent_value_min=5,
        estate_rent_value_max=100,
    ) -> None:
        self.estate_quantity = estate_quantity
        if not estates:
            self.estates = [
                Estate(
                    random.randrange(estate_buy_cost_min, estate_buy_cost_max, 1),
                    random.randrange(estate_rent_value_min, estate_rent_value_max, 1),
                )
                for _ in range(estate_quantity)
            ]
        else:
            self.estates = estates
            self.estate_quantity = len(estates)
        self.players_positions = {}
        self.full_round_value = full_round_value

    def add_players(self, players):
        for player in players:
            self.add_player(player)

    def add_player(self, player):
        self.players_positions[player] = self.FIRST_POSITION

    def move(self, player: Player, steps) -> Estate:
        position = self.players_positions[player]
        position += steps
        if position >= self.estate_quantity:
            position %= self.estate_quantity
            player.deposit(self.full_round_value)
        self.players_positions[player] = position
        return self.estates[position]

    def free_estates_from(self, player):
        for estate in self.get_estates_from(player):
            estate.free()

    def get_estates_from(self, player):
        return [e for e in self.estates if e.owner == player]

    def reset(self):
        for e in self.estates:
            e.free()
        for k, v in self.players_positions.items():
            self.players_positions[k] = self.FIRST_POSITION
