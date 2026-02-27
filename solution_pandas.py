import sqlite3
import pandas as pd

def main():
    # Connect to SQLite database
    conn = sqlite3.connect("database.db")

    # Load tables
    customers = pd.read_sql("SELECT * FROM customers", conn)
    transactions = pd.read_sql("SELECT * FROM transactions", conn)
    items = pd.read_sql("SELECT * FROM transaction_items", conn)

    # Merge tables
    df = customers.merge(transactions, on="customer_id")                   .merge(items, on="transaction_id")

    # Filter age between 18 and 35
    df = df[(df["age"] >= 18) & (df["age"] <= 35)]

    # Replace NULL quantities with 0
    df["quantity"] = df["quantity"].fillna(0)

    # Group and sum quantities
    result = df.groupby(
        ["customer_id", "age", "item_name"]
    )["quantity"].sum().reset_index()

    # Remove zero quantities
    result = result[result["quantity"] > 0]

    # Rename columns
    result.columns = ["Customer", "Age", "Item", "Quantity"]

    # Export to CSV with semicolon delimiter
    result.to_csv("output_pandas.csv", sep=";", index=False)

    conn.close()
    print("Pandas solution executed successfully. Output saved to output_pandas.csv")


if __name__ == "__main__":
    main()
