from src.player import *


def test_impulsive_strategy():
    # arrange
    strategy = ImpulsiveStrategy()
    # act
    should_buy = strategy.should_buy(100, None)
    # assert
    assert should_buy == True


def test_picky_strategy():
    # arrange
    strategy = PickyStrategy(min_rent_value=100)
    # act
    should_buy = strategy.should_buy(1000, Estate(500, 10))
    # assert
    assert should_buy == False

    # act
    should_buy = strategy.should_buy(1000, Estate(500, 100))
    # assert
    assert should_buy == False

    # act
    should_buy = strategy.should_buy(1000, Estate(500, 200))
    # assert
    assert should_buy == True


def test_cautios_strategy():
    # arrange
    strategy = CautiosStrategy(min_balance_after_buy=100)
    # act
    should_buy = strategy.should_buy(1000, Estate(500, 10))
    # assert
    assert should_buy == True

    # act
    should_buy = strategy.should_buy(1000, Estate(900, 10))
    # assert
    assert should_buy == False


def test_random_strategy():
    # arrange
    strategy = RandomStrategy()
    # act
    should_buy = strategy.should_buy(1000, Estate(500, 10))
    # assert
    assert type(should_buy) == bool


def test_player():
    # arrange
    player = Player(RandomStrategy(), balance=500)
    # act
    player.deposit(100)
    # assert
    assert player.balance == 600
    assert not player.is_broken()

    # act
    player.withdraw(300)
    # assert
    assert player.balance == 300
    assert not player.is_broken()

    # act
    player.withdraw(600)
    # assert
    assert player.balance == -300
    assert player.is_broken()
