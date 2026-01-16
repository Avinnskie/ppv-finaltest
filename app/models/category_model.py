from app.models.database import get_connection

class CategoryModel:

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categories ORDER BY id DESC")
        data = cursor.fetchall()
        conn.close()
        return data

    @staticmethod
    def create(name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO categories (name) VALUES (?)",
            (name,)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def update(category_id, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE categories SET name=? WHERE id=?",
            (name, category_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(category_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM categories WHERE id=?",
            (category_id,)
        )
        conn.commit()
        conn.close()
