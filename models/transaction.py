from db import get_db

class Transaction:
    @staticmethod
    def add(user_id, stock_symbol, transaction_type, quantity, price):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            """INSERT INTO transactions 
               (user_id, stock_symbol, transaction_type, quantity, price) 
               VALUES (?, ?, ?, ?, ?)""",
            (user_id, stock_symbol, transaction_type, quantity, price)
        )
        db.commit()
        cursor.close()

    @staticmethod
    def get_by_user(user_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM transactions WHERE user_id = ? ORDER BY transaction_date DESC", (user_id,))
        items = cursor.fetchall()
        cursor.close()
        return items
