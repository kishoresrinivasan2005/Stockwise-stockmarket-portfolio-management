from db import get_db

class PortfolioItem:
    @staticmethod
    def add(user_id, stock_symbol, company_name, quantity, buy_price, buy_date):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            """INSERT INTO portfolio 
               (user_id, stock_symbol, company_name, quantity, buy_price, buy_date) 
               VALUES (?, ?, ?, ?, ?, ?)""",
            (user_id, stock_symbol, company_name, quantity, buy_price, buy_date)
        )
        db.commit()
        item_id = cursor.lastrowid
        cursor.close()
        return item_id

    @staticmethod
    def get_by_user(user_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM portfolio WHERE user_id = ? ORDER BY buy_date DESC", (user_id,))
        items = cursor.fetchall()
        cursor.close()
        return items

    @staticmethod
    def get_by_id(portfolio_id, user_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM portfolio WHERE portfolio_id = ? AND user_id = ?", (portfolio_id, user_id))
        item = cursor.fetchone()
        cursor.close()
        return item

    @staticmethod
    def update(portfolio_id, user_id, quantity, buy_price, buy_date):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            """UPDATE portfolio 
               SET quantity = ?, buy_price = ?, buy_date = ? 
               WHERE portfolio_id = ? AND user_id = ?""",
            (quantity, buy_price, buy_date, portfolio_id, user_id)
        )
        db.commit()
        cursor.close()

    @staticmethod
    def delete(portfolio_id, user_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM portfolio WHERE portfolio_id = ? AND user_id = ?", (portfolio_id, user_id))
        db.commit()
        cursor.close()
