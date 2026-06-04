# StockWise Setup Instructions

## Prerequisites
1. Python 3.8+
2. MySQL Server (e.g. XAMPP, WAMP, or standalone MySQL)

## Database Setup
1. Start your MySQL Server.
2. The application is configured to connect to `localhost` with user `root` and an empty password by default. If you have a different setup, you can either:
   - Create a `.env` file in the root directory and set `MYSQL_USER`, `MYSQL_PASSWORD`, and `MYSQL_HOST`.
   - OR, edit `config.py` directly.

## Installation
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database (this creates tables and the default admin user):
   ```bash
   python database/init_db.py
   ```
   > **Note:** The default admin credentials are username: `admin`, password: `admin123`.

## Running the Application
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000`.

## Features Walkthrough
- **User Portal**: Register an account, log in, add stocks to your portfolio and watchlist, view the dashboard with live prices (via yfinance), view advanced analytics, and download a PDF report.
- **Admin Portal**: Go to `http://127.0.0.1:5000/admin/login` and log in with the admin credentials to view all users, manage user accounts, and see all portfolios across the system.
- **Machine Learning**: Go to the "Predictions" tab to predict the next day's stock price using a Linear Regression model.
