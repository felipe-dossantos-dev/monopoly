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


def test_player_balance():
    # arrange
    player = Player(RandomStrategy(), balance=500)
    # act
    player.deposit(100)
    # assert
    assert player.balance == 600
    assert not player.is_broken()

    # act
    player.withdraw(600)
    # assert
    assert player.balance == 0
    assert not player.is_broken()

    # act
    player.withdraw(300)
    # assert
    assert player.balance == -300
    assert player.is_broken()

    # act
    player.reset()
    # assert
    assert player.balance == 500


def test_player_buy():
    # arrange
    player_1 = Player(RandomStrategy())
    estate = Estate(100, 10)

    # act
    player_1.buy(estate)

    # assert
    assert player_1.balance == 200
    assert estate.owner == player_1


def test_player_pay_rent():
    # arrange
    player_1 = Player(RandomStrategy())
    player_2 = Player(RandomStrategy())

    estate = Estate(100, 10)
    estate.set_owner(player_2)

    # act
    player_1.pay_rent(estate)

    # assert
    assert player_1.balance == 290
    assert player_2.balance == 310


def test_player_should_buy():
    # arrange
    player = Player(ImpulsiveStrategy(), balance=500)
    assert player.should_buy(estate=Estate(501, 60)) == False
    assert player.should_buy(estate=Estate(500, 60)) == True
    assert player.should_buy(estate=Estate(499, 60)) == True