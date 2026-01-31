class EPCalculator:
    def __init__(
        self,
        suit_amount,
        principal_amount,
        suit_date,
        decree_date,
        ep_date,
        rate_suit_decree,
        rate_decree_ep,
        costs
    ):
        self.suit_amount = suit_amount
        self.principal_amount = principal_amount
        self.suit_date = suit_date
        self.decree_date = decree_date
        self.ep_date = ep_date
        self.rate_suit_decree = rate_suit_decree
        self.rate_decree_ep = rate_decree_ep
        self.costs = costs

    def days_between(self, d1, d2):
        return (d2 - d1).days

    def interest_suit_to_decree(self):
        days = self.days_between(self.suit_date, self.decree_date)
        return (self.principal_amount * self.rate_suit_decree * days) / (100 * 365)

    def interest_decree_to_ep(self):
        days = self.days_between(self.decree_date, self.ep_date)
        return (self.principal_amount * self.rate_decree_ep * days) / (100 * 365)

    def total_costs(self):
        return sum(self.costs)

    def final_amount(self):
        return (
            self.suit_amount
            + self.interest_suit_to_decree()
            + self.interest_decree_to_ep()
            + self.total_costs()
        )
