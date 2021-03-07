from src import board, player
from src.game import *
from unittest.mock import MagicMock, patch


def test_game_creation():
    # arrange
    # act
    game = Game()

    # assert
    assert len(game.players) == 4
    assert len(game.board.players_positions) == 4


def test_game_reset():
    # arrange
    game = Game()
    game.play()

    # act
    game.reset_play()

    # assert
    for p in game.players:
        assert p.balance == 300
    assert len(game.active_players) == len(game.players)
    assert game.turns_played == 0
    assert game.winner == None


def test_game_finish():
    # arrange
    game = Game()
    game.active_players = [game.players[0]]

    # act
    game.set_finish(10)

    # assert
    assert game.is_finish()
    assert game.winner == game.players[0]
    assert game.turns_played == 10


def test_remove_player():
    # arrange
    game = Game()
    player_1 = Player(RandomStrategy())
    player_2 = Player(RandomStrategy())
    game.board.estates[0].set_owner(player_1)
    game.board.estates[1].set_owner(player_1)
    game.board.estates[2].set_owner(player_2)
    game.active_players = [player_1, player_2]

    # act
    game.remove_player(player_1)

    # assert
    assert len(game.active_players) == 1
    assert game.active_players[0] == player_2
    assert not game.board.estates[0].has_owner()
    assert not game.board.estates[1].has_owner()
    assert game.board.estates[2].has_owner()


def test_play_round_pay_rent():
    # arrange
    player_1 = Player(RandomStrategy())
    player_1.play_dice = MagicMock(return_value=1)

    player_2 = Player(RandomStrategy())
    player_1.play_dice = MagicMock(return_value=1)

    game = Game(players=[player_1, player_2])
    game.active_players = [player_1, player_2]

    game.board.estates[0].set_owner(player_1)
    game.board.estates[1].set_owner(player_1)
    game.board.estates[2].set_owner(player_2)

    game.board.players_positions[player_1] = 2
    game.board.players_positions[player_2] = 3

    # act
    game.play_round()

    # assert


def test_play_round_buy():
    pass


def test_play_round_is_broken():
    pass


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