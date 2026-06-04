import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config
import sqlite3
from werkzeug.security import generate_password_hash

def init_db():
    print("Connecting to database...")
    db_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'database')
    os.makedirs(db_dir, exist_ok=True)
    db_path = os.path.join(db_dir, 'stockwise.db')
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("Reading schema.sql...")
        schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
        with open(schema_path, 'r') as f:
            sql_statements = f.read().split(';')
            
        print("Executing schema...")
        for statement in sql_statements:
            if statement.strip():
                try:
                    cursor.execute(statement)
                except Exception as e:
                    print(f"Error executing statement: {statement}")
                    print(e)
                
        conn.commit()
        
        # Create default admin user
        cursor.execute("SELECT * FROM admin WHERE username = ?", ('admin',))
        if not cursor.fetchone():
            hashed_pw = generate_password_hash('admin123')
            cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)", ('admin', hashed_pw))
            conn.commit()
            print("Default admin created (username: admin, password: admin123)")
        
        print("Database initialization complete.")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()


if __name__ == '__main__':
    init_db()
