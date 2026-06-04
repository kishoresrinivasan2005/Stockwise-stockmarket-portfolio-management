from db import get_db

class WatchlistItem:
    @staticmethod
    def add(user_id, stock_symbol, company_name):
        db = get_db()
        cursor = db.cursor()
        # Check if already exists
        cursor.execute("SELECT * FROM watchlist WHERE user_id = ? AND stock_symbol = ?", (user_id, stock_symbol))
        if cursor.fetchone():
            cursor.close()
            return False
            
        cursor.execute(
            "INSERT INTO watchlist (user_id, stock_symbol, company_name) VALUES (?, ?, ?)",
            (user_id, stock_symbol, company_name)
        )
        db.commit()
        cursor.close()
        return True

    @staticmethod
    def get_by_user(user_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM watchlist WHERE user_id = ?", (user_id,))
        items = cursor.fetchall()
        cursor.close()
        return items

    @staticmethod
    def delete(watchlist_id, user_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM watchlist WHERE watchlist_id = ? AND user_id = ?", (watchlist_id, user_id))
        db.commit()
        cursor.close()
