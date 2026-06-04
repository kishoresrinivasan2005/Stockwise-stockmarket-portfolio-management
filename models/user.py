from flask_login import UserMixin
from db import get_db

class User(UserMixin):
    def __init__(self, user_id, name, email, password):
        self.id = str(user_id)
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    @staticmethod
    def get(user_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        
        if user_data:
            return User(
                user_id=user_data['user_id'],
                name=user_data['name'],
                email=user_data['email'],
                password=user_data['password']
            )
        return None

    @staticmethod
    def find_by_email(email):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user_data = cursor.fetchone()
        cursor.close()
        
        if user_data:
            return User(
                user_id=user_data['user_id'],
                name=user_data['name'],
                email=user_data['email'],
                password=user_data['password']
            )
        return None

    @staticmethod
    def create(name, email, password):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, password)
        )
        db.commit()
        user_id = cursor.lastrowid
        cursor.close()
        return user_id

class Admin(UserMixin):
    def __init__(self, admin_id, username, password):
        self.id = f"admin_{admin_id}"
        self.admin_id = admin_id
        self.username = username
        self.password = password

    @staticmethod
    def get(admin_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM admin WHERE admin_id = ?", (admin_id,))
        admin_data = cursor.fetchone()
        cursor.close()
        
        if admin_data:
            return Admin(
                admin_id=admin_data['admin_id'],
                username=admin_data['username'],
                password=admin_data['password']
            )
        return None

    @staticmethod
    def find_by_username(username):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM admin WHERE username = ?", (username,))
        admin_data = cursor.fetchone()
        cursor.close()
        
        if admin_data:
            return Admin(
                admin_id=admin_data['admin_id'],
                username=admin_data['username'],
                password=admin_data['password']
            )
        return None
