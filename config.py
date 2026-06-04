import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key-stockwise'
    SQLITE_DB_PATH = os.environ.get('SQLITE_DB_PATH') or os.path.join(os.path.dirname(__file__), 'database', 'stockwise.db')
