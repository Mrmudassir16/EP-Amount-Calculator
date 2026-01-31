from flask import Flask, render_template, request
from datetime import datetime
from calculator.ep_calculator import EPAmountCalculator
from database import create_table, insert_case

app = Flask(__name__)
create_table()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate-ep", methods=["POST"])
def calculate_ep():
    form = request.form

    calculator = EPAmountCalculator(
        suit_amount=float(form["suit_amount"]),
        principal_amount=float(form["principal_amount"])
    )

    result = calculator.calculate_ep_amount(
        suit_date=datetime.strptime(form["suit_date"], "%Y-%m-%d"),
        decree_date=datetime.strptime(form["decree_date"], "%Y-%m-%d"),
        ep_date=datetime.strptime(form["ep_date"], "%Y-%m-%d"),
        rate1=float(form["rate1"]),
        rate2=float(form["rate2"]),
        costs={
            "costs_awarded": float(form["costs_awarded"]),
            "costs_obtaining": float(form["costs_obtaining"]),
            "court_fee_ep": float(form["court_fee_ep"]),
            "court_fee_decree": float(form["court_fee_decree"]),
            "advocate_fee_ep": float(form["advocate_fee_ep"])
        }
    )

    insert_case({
        "suit_amount": form["suit_amount"],
        "principal_amount": form["principal_amount"],
        "suit_date": form["suit_date"],
        "decree_date": form["decree_date"],
        "ep_date": form["ep_date"],
        **result
    })

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
