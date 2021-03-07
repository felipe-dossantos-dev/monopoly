from src.estate import *


def test_estate():
    # arrange
    estate = Estate(100, 10)
    assert not estate.has_owner()

    # act
    estate.buy(1)
    # assert
    assert estate.has_owner()

    # act
    estate.free()
    # assert
    assert not estate.has_owner()