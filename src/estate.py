class Estate:
    def __init__(
        self,
        buy_cost,
        rent_value,
    ) -> None:
        self.buy_cost = buy_cost
        self.rent_value = rent_value
        self.owner = None

    def has_owner(self):
        return self.owner != None

    def buy(self, player):
        self.owner = player

    def free(self):
        self.owner = None
