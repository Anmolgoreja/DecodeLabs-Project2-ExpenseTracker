# Expense Tracker

A simple Python-based **Expense Tracker** developed as **Project 2** of the DecodeLabs Python Programming Internship — Batch 2026.

## Project Overview

The Expense Tracker allows users to enter multiple expense amounts, calculate the total amount spent, and view the result.

The project focuses on **data accumulation, mathematical operations, user input, and basic program logic**.

## Features

* Add multiple expenses
* Calculate total expenses
* View total amount spent
* Validate user input
* Prevent negative and zero expenses
* Exit the program safely

## Core Concept

The project uses an accumulator to continuously update the total:

```python
total = total + expense
```

## Technologies Used

* Python
* Built-in functions and basic control structures

## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open the project folder in a terminal.
4. Run the following command:

```bash
python expense_tracker.py
```

## Example Output

```text
EXPENSE TRACKER

1. Add Expense
2. View Total Spent
3. Exit
Enter your choice (1-3): 1
Enter expense amount: 100
Expense added successfully: 100.0
Current Total Spent: 100.0

1. Add Expense
2. View Total Spent
3. Exit
Enter your choice (1-3): 1
Enter expense amount: 50
Expense added successfully: 50.0
Current Total Spent: 150.0

1. Add Expense
2. View Total Spent
3. Exit
Enter your choice (1-3): 2
Number of Expenses: 2
Total Spent: 150.0
```

## Project Structure

```text
Expense-Tracker/
├── expense_tracker.py
└── README.md
```

## Internship

**DecodeLabs — Python Programming Internship**
**Project 2 | Batch 2026**
