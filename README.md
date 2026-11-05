# Valproate Calculator (Depakene) with MySQL

Python desktop app that helps plan valproate dispensing in a public pharmacy. It considers the patient's remaining tablets, sealed boxes and monthly demand, and stores patient and dispensing history in MySQL.

> Study/portfolio project. It is a dispensing planning tool, not a diagnostic or prescribing tool.
>
> Never commit real patient data, database dumps or screenshots with personal information. Use fictitious data for demos.

## How it works

- Each box contains **50 tablets** and cannot be split.
- Tablets per month = tablets per day x 30.
- The app shows how many boxes to dispense and how many tablets remain for the following month.
- Returning patients can be searched by name, CPF or SUS number; the last balance is loaded automatically.

## Features

- Patient lookup and registration (name, CPF, SUS)
- Automatic balance retrieval for returning patients
- Dispensing history saved to MySQL
- Automatic creation of the `calculadora_valproato` database and tables (`pacientes`, `dispensacoes`)

## Stack

| Technology | Purpose |
| --- | --- |
| Python | Application logic |
| CustomTkinter | Desktop interface |
| MySQL | Patient and dispensing history |
| mysql-connector-python | MySQL driver |

## Running locally

Requirements: Python 3.10+ and MySQL Server.

```bash
git clone https://github.com/evfernandes-dev/calculadora-valproato.git
cd calculadora-valproato
pip install -r requirements.txt
python app.py
```

## Structure

```text
app.py              GUI and integration
calculadora.py      Dispensing calculation logic
database.py         MySQL connection and queries
requirements.txt    Dependencies
```

## Limitations and next steps

- Database credentials are defined in `database.py`; move them to environment variables before using real data.
- Add schema migrations instead of creating tables at startup.
- Add tests for the dispensing rules.
- Add a screenshot or short GIF.
- Add an export/backup routine.

## Author

**Emanuel Vitor Fernandes Nascimento**

[LinkedIn](https://www.linkedin.com/in/emanuel-vitor-fernandes-6a3796421) · [GitHub](https://github.com/evfernandes-dev)
