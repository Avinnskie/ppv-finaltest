from app.models.database import get_connection
from datetime import datetime

class TransactionModel:

    @staticmethod
    def create_transaction(items):
        """
        items = [
            {product_id, price, quantity, subtotal}
        ]
        """
        conn = get_connection()
        cursor = conn.cursor()

        total = sum(item["subtotal"] for item in items)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            INSERT INTO transactions (date, total)
            VALUES (?, ?)
        """, (date, total))

        transaction_id = cursor.lastrowid

        for item in items:
            cursor.execute("""
                INSERT INTO transaction_details
                (transaction_id, product_id, quantity, subtotal)
                VALUES (?, ?, ?, ?)
            """, (
                transaction_id,
                item["product_id"],
                item["quantity"],
                item["subtotal"]
            ))

            cursor.execute("""
                UPDATE products
                SET stock = stock - ?
                WHERE id = ?
            """, (item["quantity"], item["product_id"]))

        conn.commit()
        conn.close()
