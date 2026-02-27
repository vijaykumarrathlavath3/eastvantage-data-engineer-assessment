import sqlite3
import pandas as pd

def main():
    # Connect to SQLite database
    conn = sqlite3.connect("database.db")

    query = """
    SELECT 
        c.customer_id AS Customer,
        c.age AS Age,
        ti.item_name AS Item,
        SUM(COALESCE(ti.quantity,0)) AS Quantity
    FROM customers c
    JOIN transactions t ON c.customer_id = t.customer_id
    JOIN transaction_items ti ON t.transaction_id = ti.transaction_id
    WHERE c.age BETWEEN 18 AND 35
    GROUP BY c.customer_id, ti.item_name
    HAVING Quantity > 0
    ORDER BY c.customer_id;
    """

    df = pd.read_sql_query(query, conn)

    # Export to CSV with semicolon delimiter
    df.to_csv("output_sql.csv", sep=";", index=False)

    conn.close()
    print("SQL solution executed successfully. Output saved to output_sql.csv")


if __name__ == "__main__":
    main()
