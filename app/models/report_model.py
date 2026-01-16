from app.models.database import get_connection

class ReportModel:

    @staticmethod
    def get_transactions():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, date, total
            FROM transactions
            ORDER BY date DESC
        """)

        data = cursor.fetchall()
        conn.close()
        return data

    @staticmethod
    def get_transaction_detail(transaction_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT products.name, transaction_details.quantity,
                   transaction_details.subtotal
            FROM transaction_details
            JOIN products ON transaction_details.product_id = products.id
            WHERE transaction_details.transaction_id = ?
        """, (transaction_id,))

        data = cursor.fetchall()
        conn.close()
        return data
