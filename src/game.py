from src.player import *
from src.board import *
import json


class GameResult:
    def __init__(self, timeout_finish, turns_played, winner_strategy) -> None:
        self.timeout_finish = timeout_finish
        self.turns_played = turns_played
        self.winner_strategy = winner_strategy

    def __repr__(self) -> str:
        return json.dumps(self.__dict__, indent=2)


class Game:
    def __init__(self, players=None, board=None, max_rounds=1000) -> None:
        self.players = players
        if not players:
            self.players = [
                Player(ImpulsiveStrategy()),
                Player(PickyStrategy()),
                Player(CautiosStrategy()),
                Player(RandomStrategy()),
            ]

        if not board:
            self.board = Board()
        self.board.add_players(self.players)

        self.winner = None
        self.turns_played = 0
        self.max_rounds = max_rounds

    def play(self):
        self.reset_play()
        for i in range(0, self.max_rounds):
            if self.is_finish():
                self.set_finish(i)
                timeout_finish = False
                break
            self.play_round()

        if not self.winner:
            self.active_players.sort(key=lambda x: x.balance, reverse=True)
            self.set_finish(self.max_rounds)
            timeout_finish = True

        return GameResult(
            timeout_finish=timeout_finish,
            turns_played=self.turns_played,
            winner_strategy=type(self.winner.strategy).__name__,
        )

    def reset_play(self):
        self.reset_players()
        self.board.reset()
        self.active_players = self.players.copy()
        self.turns_played = 0
        self.winner = None

    def reset_players(self):
        for player in self.players:
            player.reset()

    def is_finish(self):
        return len(self.active_players) == 1

    def set_finish(self, turn):
        self.winner = self.active_players[0]
        self.turns_played = turn

    def play_round(self):
        for player in self.active_players:
            dice_value = player.play_dice()
            estate = self.board.move(player, dice_value)
            if estate.has_owner():
                player.pay_rent(estate)
            elif player.should_buy(estate):
                player.buy(estate)
            if player.is_broken():
                self.remove_player(player)

    def remove_player(self, player):
        self.board.free_estates_from(player)
        self.active_players.remove(player)
