from src.board import *
from src.player import *


def test_board_estates():
    # arrange
    # act
    board = Board()
    # assert
    assert len(board.estates) == board.estate_quantity


def test_board_add_players():
    # arrange
    board = Board()
    # act
    player = Player(RandomStrategy())
    board.add_player(player)
    # assert
    assert len(board.players_positions) == 1
    assert board.players_positions[player] == Board.FIRST_POSITION

    # act
    player = Player(RandomStrategy())
    board.add_players([player, Player(RandomStrategy())])
    # assert
    assert len(board.players_positions) == 3
    assert board.players_positions[player] == Board.FIRST_POSITION


def test_board_move_player():
    # arrange
    board = Board(estate_quantity=20, full_round_value=100)
    player = Player(RandomStrategy(), balance=300)
    board.add_player(player)

    # act
    estate = board.move_player(player, 4)
    # assert
    assert board.players_positions[player] == 4
    assert estate != None
    assert type(estate) == Estate

    # act
    board.move_player(player, 20)
    # assert
    assert board.players_positions[player] == 4
    assert player.balance == 400
    assert estate != None
    assert type(estate) == Estate