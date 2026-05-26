from flask import Flask, render_template, request, redirect, url_for, Response
from datetime import datetime
import csv
import io

from calculator.ep_calculator import EPCalculator
from database import init_db, save_case, get_all_cases, delete_case

app = Flask(__name__)

# Initialize database
init_db()


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    breakdown = None

    if request.method == "POST":
        try:
            # Amounts
            suit_amount = float(request.form["suit_amount"])
            principal_amount = float(request.form["principal_amount"])

            # Dates
            suit_date = datetime.strptime(request.form["suit_date"], "%Y-%m-%d")
            decree_date = datetime.strptime(request.form["decree_date"], "%Y-%m-%d")
            ep_date = datetime.strptime(request.form["ep_date"], "%Y-%m-%d")

            # Validation
            if suit_date > decree_date:
                error = "Validation Error: Decree Date cannot be before the Suit Filing Date."
            elif decree_date > ep_date:
                error = "Validation Error: EP Filing Date cannot be before the Decree Date."
            else:
                # Interest rates
                rate_suit_decree = float(request.form["rate_suit_decree"])
                rate_decree_ep = float(request.form["rate_decree_ep"])

                # Contested status
                suit_contested = request.form.get("suit_contested", "Yes")

                # Costs
                costs_awarded = float(request.form["costs_awarded"])
                cost_obtaining = float(request.form["cost_obtaining"])
                court_fee_ep = float(request.form["court_fee_ep"])
                court_fee_decree = float(request.form["court_fee_decree"])
                advocate_fee_ep = float(request.form["advocate_fee_ep"])

                costs = [
                    costs_awarded,
                    cost_obtaining,
                    court_fee_ep,
                    court_fee_decree,
                    advocate_fee_ep,
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

                # Calculate standard Main Advocate Fee (Decree reference) and EP Advocate Fee (1/4 of Main)
                std_main_fee = EPCalculator.calculate_advocate_fee(suit_amount, suit_contested)
                std_ep_fee = round(std_main_fee / 4.0, 2)
                is_auto_calculated = abs(advocate_fee_ep - std_ep_fee) < 0.05

                if is_auto_calculated:
                    status_lbl = "Contested: 1/4 of Full" if suit_contested == "Yes" else "Non-Contested: 1/4 of Half"
                    fee_details = f"Auto-Sync ({status_lbl})"
                else:
                    fee_details = f"Manual Override (Standard EP: ₹{std_ep_fee:.2f})"

                # Detailed breakdown for visual layout
                breakdown = {
                    "suit_amount": suit_amount,
                    "principal_amount": principal_amount,
                    "interest_suit_decree": round(calculator.interest_suit_to_decree(), 2),
                    "interest_decree_ep": round(calculator.interest_decree_to_ep(), 2),
                    "advocate_fee_ep": advocate_fee_ep,
                    "advocate_fee_details": fee_details,
                    "total_costs": round(calculator.total_costs(), 2),
                    "final_amount": result
                }

                # Save all detailed case fields to SQLite database
                save_case(
                    suit_amount=suit_amount,
                    principal_amount=principal_amount,
                    suit_date=request.form["suit_date"],
                    decree_date=request.form["decree_date"],
                    ep_date=request.form["ep_date"],
                    rate_suit_decree=rate_suit_decree,
                    rate_decree_ep=rate_decree_ep,
                    costs_awarded=costs_awarded,
                    cost_obtaining=cost_obtaining,
                    court_fee_ep=court_fee_ep,
                    court_fee_decree=court_fee_decree,
                    advocate_fee_ep=advocate_fee_ep,
                    suit_contested=suit_contested,
                    final_amount=result
                )
        except Exception as e:
            error = f"Error during calculation: {str(e)}"

    # Retrieve all cases for the history feed
    cases = get_all_cases()

    return render_template(
        "index.html",
        result=result,
        error=error,
        breakdown=breakdown,
        cases=cases,
        form_data=request.form if error else {}
    )


@app.route("/delete/<int:case_id>", methods=["POST"])
def delete(case_id):
    delete_case(case_id)
    return redirect(url_for("index"))


@app.route("/export")
def export_cases():
    cases = get_all_cases()
    
    # Generate CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow([
        "ID", "Suit Amount (INR)", "Principal Amount (INR)", 
        "Suit Date", "Decree Date", "EP Date", 
        "Suit to Decree Rate (%)", "Decree to EP Rate (%)", 
        "Costs Awarded (INR)", "Cost of Obtaining (INR)", 
        "Court Fee EP (INR)", "Court Fee Decree (INR)", 
        "Advocate Fee EP (INR)", "Suit Contested", 
        "EP Payable (INR)", "Created At"
    ])
    
    # Write rows
    for case in cases:
        writer.writerow([
            case.get("id"),
            case.get("suit_amount"),
            case.get("principal_amount"),
            case.get("suit_date"),
            case.get("decree_date"),
            case.get("ep_date"),
            case.get("rate_suit_decree"),
            case.get("rate_decree_ep"),
            case.get("costs_awarded"),
            case.get("cost_obtaining"),
            case.get("court_fee_ep"),
            case.get("court_fee_decree"),
            case.get("advocate_fee_ep"),
            case.get("suit_contested"),
            case.get("final_amount"),
            case.get("created_at")
        ])
    
    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=ep_cases_history.csv"}
    )


if __name__ == "__main__":
    app.run(debug=True)

