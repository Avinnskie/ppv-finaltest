from app.models.database import get_connection

class ProductModel:

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT products.id, products.category_id, products.name, products.price, products.stock,
                   categories.name AS category_name
            FROM products
            LEFT JOIN categories ON products.category_id = categories.id
            ORDER BY products.id DESC
        """)
        rows = cursor.fetchall()
        conn.close()
        
        return [
            {
                "id": row[0],
                "category_id": row[1],
                "name": row[2],
                "price": row[3],
                "stock": row[4],
                "category_name": row[5] if row[5] else "Tanpa Kategori"
            }
            for row in rows
        ]

    @staticmethod
    def create(category_id, name, price, stock):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO products (category_id, name, price, stock)
            VALUES (?, ?, ?, ?)
        """, (category_id, name, price, stock))
        conn.commit()
        conn.close()

    @staticmethod
    def update(product_id, category_id, name, price, stock):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE products
            SET category_id=?, name=?, price=?, stock=?
            WHERE id=?
        """, (category_id, name, price, stock, product_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(product_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM products WHERE id=?",
            (product_id,)
        )
        conn.commit()
        conn.close()
