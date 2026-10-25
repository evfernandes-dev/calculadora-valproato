# Valproate Calculator (Depakene) with MySQL Integration

Desktop application developed in **Python** to help plan the dispensing of **Valproate**, taking into account the amount of medication the patient already has, the fact that medication is distributed in sealed boxes, and integrating with **MySQL** for patient record management and dispensing history.

The goal is to make the dispensing process more organized, reduce waste, make better use of available medication, and maintain a complete audit trail of patient dispensations.

---

## What's New (MySQL Integration & Patient ID)

- **Patient Identification**: Top-level field to search or register patients by Name, CPF, or SUS.
- **Automatic Balance Retrieval**: When a returning patient is looked up, the system automatically fetches their last remaining balance (`sobra final`) and sets it as the initial balance for the new calculation.
- **Dispensing History**: Save calculation and dispensing records directly to MySQL.
- **MySQL Database Support**: Automatically creates and manages the `calculadora_valproato` database and tables (`pacientes`, `dispensacoes`).

---

## Why this project was created

The calculator was developed to support the dispensing routine in a public pharmacy.

In some cases, patients still have tablets left from a previous dispensing period. Before giving out new boxes, this remaining amount can be considered when planning the following months.

The application automates this calculation and helps visualize:
- patient identification and history;
- how many tablets the patient already has;
- how many tablets are required each month;
- how many boxes need to be dispensed;
- how many tablets will remain for the following month.

---

## How it works

The application assumes that:
- each box contains **50 tablets**;
- boxes cannot be split;
- the number of months to plan is defined;
- the number of tablets per day is entered, which automatically fills in the required tablets per month (**tablets per day x 30**);
- patient records and initial balances can be loaded from MySQL.

---

## Technologies used

| Technology | Purpose |
|---|---|
| Python | Main application logic |
| CustomTkinter | Graphical user interface |
| MySQL | Patient records and dispensing history database |
| mysql-connector-python | MySQL driver for Python |
| Git & GitHub | Version control and project hosting |

---

## Project structure

```text
calculadora-valproato/
│
├── app.py              # Graphical user interface & integration
├── calculadora.py      # Dispensing calculation logic
├── database.py         # MySQL connection & queries
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## How to run

### Requirements

- Python 3.10 or higher
- MySQL Server (running locally, e.g., via WAMP, XAMPP, or standalone MySQL)

### 1. Clone the repository

```bash
git clone https://github.com/evfernandes-dev/calculadora-valproato.git
```

### 2. Open the project folder

```bash
cd calculadora-valproato
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

---

## Author

**Emanuel Vitor Fernandes Nascimento**

Back-End Developer | Automation

[LinkedIn](https://www.linkedin.com/in/emanuel-vitor-fernandes-6a3796421) · [GitHub](https://github.com/evfernandes-dev)
