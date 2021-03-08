from collections import Counter
from statistics import mean
import json
from src.board import Board
from src.game import Game


class SimulationResult:
    def __init__(self, game_results) -> None:
        self.total_games = len(game_results)
        self.strategy_counter = Counter([r.winner_strategy for r in game_results])
        self.winner_strategy = max(self.strategy_counter, key=self.strategy_counter.get)
        self.timeout_counter = Counter([r.timeout_finish for r in game_results])
        self.strategy_percentage = dict(
            [(k, v / self.total_games * 100) for k, v in self.strategy_counter.items()]
        )
        self.mean_turns = mean([r.turns_played for r in game_results])
        self.timeout_per_thousands = (
            self.timeout_counter[True] / self.total_games * 1000
        )

    def __repr__(self) -> str:
        return json.dumps(self.__dict__, indent=2)


class Simulation:
    def __init__(
        self, number_of_games=300, max_rounds=1000, players=None, estates=None, **kwargs
    ):
        self.number_of_games = number_of_games
        self.max_rounds = max_rounds
        self.players = players
        self.board = None
        if estates:
            self.board = Board(estates=estates, **kwargs)

    def simulate(self):
        game_results = []
        for i in range(self.number_of_games):
            print(f"running game {i}")
            game = Game(
                players=self.players, board=self.board, max_rounds=self.max_rounds
            )
            game_result = game.play()
            game_results.append(game_result)
        return SimulationResult(game_results)