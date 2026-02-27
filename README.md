# Eastvantage Data Engineer Assessment

## Overview

This repository contains two separate solutions for the assignment:

1.  Pure SQL solution (`solution_sql.py`)
2.  Pandas solution (`solution_pandas.py`)

Both solutions: - Connect to a SQLite database named `database.db` -
Extract total quantities of each item bought per customer aged 18-35 -
Exclude items with total quantity = 0 - Export results to CSV using
semicolon (`;`) delimiter

------------------------------------------------------------------------

## Database Assumption

The database contains the following tables:

-   customers (customer_id, age)
-   transactions (transaction_id, customer_id)
-   transaction_items (transaction_id, item_name, quantity)

------------------------------------------------------------------------

## How to Run

Place your SQLite database file as:

    database.db

Then run:

    python solution_sql.py

or

    python solution_pandas.py

------------------------------------------------------------------------

## Output

Each script generates:

-   output_sql.csv
-   output_pandas.csv

Format:

Customer;Age;Item;Quantity

------------------------------------------------------------------------

## Python Version

Python 3.9+ recommended.
