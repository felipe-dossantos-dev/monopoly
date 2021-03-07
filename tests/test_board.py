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
    estate = board.move(player, 4)
    # assert
    assert board.players_positions[player] == 4
    assert estate != None
    assert type(estate) == Estate

    # act
    estate = board.move(player, 20)
    # assert
    assert board.players_positions[player] == 4
    assert player.balance == 400
    assert estate != None
    assert type(estate) == Estate

    # act
    board.reset()
    # assert
    assert board.players_positions[player] == 0


def test_board_free_estates_from():
    # arrange
    player_1 = Player(RandomStrategy())
    estate_1 = Estate(100, 10)
    estate_1.set_owner(player_1)

    player_2 = Player(RandomStrategy())
    estate_2 = Estate(100, 10)
    estate_2.set_owner(player_2)
    estate_3 = Estate(100, 10)
    estate_3.set_owner(player_2)
    board = Board(estates=[estate_1, estate_2, estate_3])

    # act
    board.free_estates_from(player_1)

    # assert
    assert estate_1.has_owner() == False

    # act
    board.reset()

    # assert
    assert estate_1.has_owner() == False
    assert estate_2.has_owner() == False
    assert estate_3.has_owner() == False