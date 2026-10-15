# Valproate Calculator (Depakene)

Desktop application developed in **Python** to help plan the dispensing of **Valproate 250 mg and 500 mg**, taking into account the amount of medication the patient already has and the fact that medication is distributed in sealed boxes.

The goal is to make the dispensing process more organized, reduce waste, and make better use of the available medication.

---

## Why this project was created

The calculator was developed to support the dispensing routine in a public pharmacy.

In some cases, patients still have tablets left from a previous dispensing period. Before giving out new boxes, this remaining amount can be considered when planning the following months.

The application automates this calculation and helps visualize:

- how many tablets the patient already has;
- how many tablets are required each month;
- how many boxes need to be dispensed;
- how many tablets will remain for the following month.

This reduces manual calculations and helps minimize errors during medication dispensing planning.

---

## How it works

The application assumes that:

- each box contains **50 tablets**;
- boxes cannot be split;
- the user selects the medication strength: **250 mg or 500 mg**;
- the number of months to plan is defined;
- the required number of tablets per month is entered;
- an initial remaining balance already available to the patient can also be entered.

Based on this information, the system performs the calculation month by month.

### Basic flow

```text
Patient data
      ↓
Required amount per month
      ↓
Available balance
      ↓
Calculation of required boxes
      ↓
Remaining balance for the next month
```

---

## Example

Suppose the patient needs:

```text
60 tablets per month
```

and already has:

```text
20 tablets
```

The program first considers these 20 tablets and calculates only the additional amount required.

Since each box contains 50 tablets, the application determines how many sealed boxes must be dispensed and how many tablets will remain available for the next period.

---

## Interface

The application includes a graphical user interface developed with **CustomTkinter**, so calculations can be performed without using the terminal.

The interface was designed to be simple, fast, and practical for the daily dispensing routine.

---

## Technologies used

| Technology | Purpose |
|---|---|
| Python | Main application logic |
| CustomTkinter | Graphical user interface |
| Git | Version control |
| GitHub | Project hosting and documentation |

---

## Project structure

```text
calculadora-valproato/
│
├── app.py              # Graphical user interface
├── calculadora.py      # Dispensing calculation logic
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## How to run

### Requirements

Make sure you have installed:

```text
Python 3.10 or higher
```

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

## Dependencies

The project mainly uses:

```text
customtkinter
```

All required dependencies can be installed automatically using `requirements.txt`.

---

## Main goals

- Reduce manual calculations.
- Make medication dispensing planning easier.
- Use the patient's existing medication balance before dispensing new boxes.
- Reduce medication waste.
- Support better management of public resources.
- Make the process faster and more standardized.

---

## Future improvements

- [x] Calculation based on the number of tablets.
- [x] Initial balance consideration.
- [x] Month-by-month planning.
- [x] Graphical user interface.
- [ ] Generate dispensing reports.
- [ ] Export results to PDF.
- [ ] Save calculation history.
- [ ] Add more complete input validation.
- [ ] Create a Windows installer.
- [ ] Generate a `.exe` executable.
- [ ] Add automated tests.

---

## Disclaimer

This application is an **administrative and operational support tool for quantity calculations**.

It does not provide prescriptions, diagnoses, dosage changes, or therapeutic recommendations.

Medication dispensing must follow the prescription provided, applicable protocols, and the instructions of the responsible healthcare professionals.

---

## Author

**Emanuel Vitor Fernandes Nascimento**

Back-End Developer | Automation

[LinkedIn](https://www.linkedin.com/in/emanuel-vitor-fernandes-6a3796421) · [GitHub](https://github.com/evfernandes-dev)

---

## About the project

This project was created from a real-world need, using programming to automate a repetitive calculation and support an actual work routine.

In addition to its practical application, the project also involves concepts related to **Python, programming logic, graphical user interfaces, code organization, and software development for solving real-world problems**.
