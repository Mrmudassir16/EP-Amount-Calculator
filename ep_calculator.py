from datetime import datetime


class EPAmountCalculator:
    def __init__(self, suit_amount, principal_amount):
        self.suit_amount = suit_amount
        self.principal_amount = principal_amount
        self.interest_phase1 = 0
        self.interest_phase2 = 0
        self.total_costs = 0

    @staticmethod
    def days_between(d1, d2):
        return (d2 - d1).days

    def calculate_phase1_interest(self, suit_date, decree_date, rate):
        days = self.days_between(suit_date, decree_date)
        self.interest_phase1 = (
            self.principal_amount * rate * days
        ) / (100 * 365)
        return self.interest_phase1

    def calculate_phase2_interest(self, decree_date, ep_date, rate):
        days = self.days_between(decree_date, ep_date)
        self.interest_phase2 = (
            self.principal_amount * rate * days
        ) / (100 * 365)
        return self.interest_phase2

    def calculate_costs(
        self,
        costs_awarded,
        costs_obtaining,
        court_fee_ep,
        court_fee_decree,
        advocate_fee_ep
    ):
        self.total_costs = (
            costs_awarded
            + costs_obtaining
            + court_fee_ep
            + court_fee_decree
            + advocate_fee_ep
        )
        return self.total_costs

    def final_ep_amount(self):
        return (
            self.suit_amount
            + self.interest_phase1
            + self.interest_phase2
            + self.total_costs
        )
