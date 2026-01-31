from datetime import datetime


class EPAmountCalculator:
    def __init__(self, suit_amount, principal_amount):
        self.suit_amount = suit_amount
        self.principal_amount = principal_amount

    @staticmethod
    def days_between(d1, d2):
        return (d2 - d1).days

    def interest(self, start_date, end_date, rate):
        days = self.days_between(start_date, end_date)
        return (self.principal_amount * rate * days) / (100 * 365)

    def total_costs(self, costs):
        return sum(costs.values())

    def calculate_ep_amount(
        self,
        suit_date,
        decree_date,
        ep_date,
        rate1,
        rate2,
        costs
    ):
        interest_1 = self.interest(suit_date, decree_date, rate1)
        interest_2 = self.interest(decree_date, ep_date, rate2)
        total_cost = self.total_costs(costs)

        final_amount = (
            self.suit_amount
            + interest_1
            + interest_2
            + total_cost
        )

        return {
            "phase1_interest": round(interest_1, 2),
            "phase2_interest": round(interest_2, 2),
            "total_costs": round(total_cost, 2),
            "ep_amount": round(final_amount, 2)
        }
