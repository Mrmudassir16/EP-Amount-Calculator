# Execution Petition (EP) Amount Calculator - Premium Legal Dashboard

A premium, full-stack legal automation web application designed for advocates to calculate, audit, and log court **Execution Petition (EP) amounts** based on real-world Indian legal procedures and official fee slabs.

This application features a gorgeous glassmorphism UI, a real-time responsive calculation engine, automatic SQLite database history cataloging, and painless spreadsheet exporting.

---

## ⚖️ Advanced Advocate Fee Engine (AP Money Suits Slabs)

The calculator implements the official **Andhra Pradesh Advocate Fee (Money Suits)** tiered rules, ensuring absolute mathematical accuracy for legal audits:

### 1. The Core Slabs
* **10%** on the first ₹10,000 *(Max ₹1,000)*
* **7%** on the next ₹10,000 *(Max ₹700)*
* **5%** on the next ₹30,000 *(Max ₹1,500)*
* **3%** on the remaining amount

### 2. Contested vs. Non-Contested Modifier
* **Contested (Yes)**: Returns the **100% full fee** of the calculated slabs.
* **Non-Contested (No)**: Returns exactly **50% (half fee)** of the calculated slabs.

### 3. Decree Reference vs. EP Sync Distinction
To match real-life court filing procedures, the application distinguishes between:
* **Decree Advocate Fee (Reference)**: Displayed as a dynamic indigo information card right under the amount fields. This calculates the original suit advocate fee so you can easily sum it with other minor trial costs and enter the total in the **"Costs Awarded in Decree"** field.
* **Advocate Fee in EP (Auto-Synced)**: Legally defined as **exactly 1/4 (25%)** of the Decree Advocate Fee. The "Advocate Fee in EP" input field automatically populates with this 1/4 synced value in real-time, featuring a manual override check-toggle.

---

## 🚀 Premium Features

* **Phase-Wise Interest Calculator**: Computes interest on the principal amount across litigation milestones:
  * **Phase 1**: Suit Filing Date ➔ Decree Date (Pre-Decree Interest)
  * **Phase 2**: Decree Date ➔ EP Filing Date (Post-Decree Interest)
* **Interactive Responsive Interface**: 
  * Sleek glassmorphism card panels with legal-themed dynamic backdrop slideshows.
  * Real-time client-side calculation triggers that sync the EP fee as you type.
  * **Auto-Reset Stale Results**: Modifying the form instantly clears the old calculation and displays a beautifully formatted **Litigation Quick Guide** checklist.
* **Dual Database & Spreadsheet Architecture**:
  * **SQLite Relational Backend**: Every calculated petition record is securely audited in a local `ep_cases.db` database.
  * **1-Click Excel Export**: A premium "Export to Excel (CSV)" button dynamically compiles your SQLite history into a standard spreadsheet compatible with Microsoft Excel and Google Sheets.
  * **Audit History Feed**: An elegant log table with inline record filtering and secure row deletions.

---

## 🛠️ Tech Stack

* **Backend**: Python, Flask (Robust MVC-style structure)
* **Frontend**: HTML5, Vanilla CSS3 (Custom Glassmorphism Design System), JavaScript (Reactive DOM Events)
* **Database**: SQLite3 (Self-migrating schema model)
* **Spreadsheet Compiler**: Python Standard Library CSV Engine

---

## 📁 Project Structure

```bash
EP-Amount-Calculator/
│
├── app.py                  # Flask Application Controller & API Routes
├── database.py             # SQLite Schema Definitions & Database CRUD operations
├── requirements.txt        # Python dependency manifest (Flask)
├── .gitignore              # Git ignore rules
├── README.md               # Dynamic Project Documentation
│
├── calculator/
│   ├── __init__.py
│   └── ep_calculator.py    # Core OOP interest and advocate fee mathematical calculations
│
├── templates/
│   └── index.html          # Custom Glassmorphic Litigation Dashboard & Reactive JS
│
└── static/
    └── images/             # Premium legal-themed background slide deck assets
```

---

## 💻 Getting Started

### Prerequisites
* Python 3.8 or higher installed on your computer.

### 1. Installation
Clone the repository and navigate into the project directory:
```bash
git clone https://github.com/Mrmudassir16/EP-Amount-Calculator.git
cd EP-Amount-Calculator
```

Create a virtual environment and activate it:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

### 2. Running the Application
Launch the Flask development server:
```bash
python app.py
```
Open your browser and navigate to: **`http://127.0.0.1:5000`**

---

## 📄 License
This software is developed for legal practitioners and advocates to streamline litigation documentation. All rights reserved.
