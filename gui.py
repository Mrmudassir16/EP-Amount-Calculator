import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from ep_calculator import EPAmountCalculator


def calculate_ep():
    try:
        calculator = EPAmountCalculator(
            float(suit_amount.get()),
            float(principal_amount.get())
        )

        suit_dt = datetime.strptime(suit_date.get(), "%d-%m-%Y")
        decree_dt = datetime.strptime(decree_date.get(), "%d-%m-%Y")
        ep_dt = datetime.strptime(ep_date.get(), "%d-%m-%Y")

        calculator.calculate_phase1_interest(
            suit_dt, decree_dt, float(rate1.get())
        )

        calculator.calculate_phase2_interest(
            decree_dt, ep_dt, float(rate2.get())
        )

        calculator.calculate_costs(
            float(cost_awarded.get()),
            float(cost_obtaining.get()),
            float(cf_ep.get()),
            float(cf_decree.get()),
            float(adv_fee.get())
        )

        final_amount = calculator.final_ep_amount()

        result_label.config(
            text=f"EP Amount Payable: ₹ {final_amount:.2f}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------- GUI ----------
root = tk.Tk()
root.title("AP EP Amount Calculator")
root.geometry("420x620")

def add_label_entry(text):
    tk.Label(root, text=text).pack()
    entry = tk.Entry(root)
    entry.pack()
    return entry


tk.Label(root, text="EP AMOUNT CALCULATOR", font=("Arial", 14, "bold")).pack(pady=10)

suit_amount = add_label_entry("Suit Amount (₹)")
principal_amount = add_label_entry("Principal Amount (₹)")

suit_date = add_label_entry("Suit Filing Date (DD-MM-YYYY)")
decree_date = add_label_entry("Decree Date (DD-MM-YYYY)")
ep_date = add_label_entry("EP Filing Date (DD-MM-YYYY)")

rate1 = add_label_entry("Interest Rate % (Suit → Decree)")
rate2 = add_label_entry("Interest Rate % (Decree → EP)")

cost_awarded = add_label_entry("Costs Awarded in Decree (₹)")
cost_obtaining = add_label_entry("Cost for Obtaining Decree (₹)")
cf_ep = add_label_entry("Court Fee on EP (₹)")
cf_decree = add_label_entry("Court Fee on Decree (₹)")
adv_fee = add_label_entry("Advocate Fee in EP (₹)")

tk.Button(root, text="Calculate EP Amount", command=calculate_ep).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
