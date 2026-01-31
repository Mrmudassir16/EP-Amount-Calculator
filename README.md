# Execution Petition (EP) Amount Calculator

A full-stack web application built using Flask to calculate court Execution Petition (EP) amounts based on real-world legal formulas.

This project automates interest calculation across different legal phases and stores case records using SQLite.

---

## 🚀 Features

- Execution Petition amount calculation
- Phase-wise interest calculation
  - Suit Filing Date → Decree Date
  - Decree Date → EP Date
- Cost aggregation (court fees, advocate fees, etc.)
- SQLite database for storing EP cases
- Simple HTML frontend
- Clean OOP-based business logic
- Flask backend with server-side rendering

---

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Architecture:** OOP + MVC-style separation
- **Version Control:** Git & GitHub

---

## 📁 Project Structure

EP-Amount-Calculator/
│
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
│
├── calculator/
│ ├── init.py
│ └── ep_calculator.py
│
├── templates/
│ └── index.html
│
└── static/

