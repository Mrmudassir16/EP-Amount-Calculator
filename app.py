from flask import Flask, render_template, request
from datetime import datetime

from calculator.ep_calculator import EPCalculator
from database import init_db, save_case

app = Flask(__name__)

# Initialize database
init_db()


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        # Amounts
        suit_amount = float(request.form["suit_amount"])
        principal_amount = float(request.form["principal_amount"])

        # Dates
        suit_date = datetime.strptime(request.form["suit_date"], "%Y-%m-%d")
        decree_date = datetime.strptime(request.form["decree_date"], "%Y-%m-%d")
        ep_date = datetime.strptime(request.form["ep_date"], "%Y-%m-%d")

        # Interest rates
        rate_suit_decree = float(request.form["rate_suit_decree"])
        rate_decree_ep = float(request.form["rate_decree_ep"])

        # Costs
        costs = [
            float(request.form["costs_awarded"]),
            float(request.form["cost_obtaining"]),
            float(request.form["court_fee_ep"]),
            float(request.form["court_fee_decree"]),
            float(request.form["advocate_fee_ep"]),
        ]

        # Calculator object
        calculator = EPCalculator(
            suit_amount=suit_amount,
            principal_amount=principal_amount,
            suit_date=suit_date,
            decree_date=decree_date,
            ep_date=ep_date,
            rate_suit_decree=rate_suit_decree,
            rate_decree_ep=rate_decree_ep,
            costs=costs
        )

        # Final amount
        result = round(calculator.final_amount(), 2)

        # Save to database
        save_case(suit_amount, principal_amount, result)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
