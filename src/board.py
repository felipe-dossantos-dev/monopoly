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
        estate_buy_cost_factor=500,
        estate_rent_value_factor=100,
    ) -> None:
        self.estate_quantity = estate_quantity
        self.estates = estates
        if not estates:
            self.estates = [
                Estate(
                    random.random() * estate_buy_cost_factor,
                    random.random() * estate_rent_value_factor,
                )
                for _ in range(estate_quantity)
            ]
        self.players_positions = {}
        self.full_round_value = full_round_value

    def add_players(self, players):
        for player in players:
            self.add_player(player)

    def add_player(self, player):
        self.players_positions[player] = self.FIRST_POSITION

    def move_player(self, player: Player, steps) -> Estate:
        position = self.players_positions[player]
        position += steps
        if position >= self.estate_quantity:
            position %= self.estate_quantity
            player.deposit(self.full_round_value)
        self.players_positions[player] = position
        return self.estates[position]