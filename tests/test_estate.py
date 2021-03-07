from src.player import Player
from src.estate import *
from src.player import *


def test_estate():
    # arrange
    player = Player(RandomStrategy(), balance=300)
    estate = Estate(100, 10)
    assert not estate.has_owner()

    # act
    estate.set_owner(player)
    # assert
    assert estate.has_owner()

    # act
    estate.pay_rent()
    # assert
    assert player.balance == 310

    # act
    estate.free()
    # assert
    assert not estate.has_owner()