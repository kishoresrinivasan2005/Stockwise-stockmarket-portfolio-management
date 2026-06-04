
# 📈 StockWise – Stock Market Portfolio Management System

StockWise is a full-stack web application that enables investors to efficiently manage their stock portfolios, track investments, monitor profits and losses, maintain watchlists, and analyze portfolio performance through an intuitive dashboard.

Built using Flask, MySQL, HTML, CSS, Bootstrap, and Python, StockWise provides a practical solution for personal investment tracking and portfolio management.

---

## 🚀 Features

### 🔐 User Authentication
- User Registration
- Secure Login & Logout
- Password Hashing
- Session Management

### 📊 Dashboard
- Total Investment Overview
- Portfolio Value Tracking
- Profit/Loss Analysis
- Number of Stocks Held
- Best Performing Stock

### 💼 Portfolio Management
- Add Stocks
- Edit Holdings
- Delete Holdings
- View Portfolio Summary
- Track Investment Performance

### ⭐ Watchlist
- Add Stocks to Watchlist
- Remove Stocks
- Monitor Favorite Stocks

### 📜 Transaction Management
- Record Buy Transactions
- Record Sell Transactions
- View Transaction History

### 📈 Portfolio Analytics
- Portfolio Allocation Analysis
- Investment Trend Tracking
- Monthly Performance Reports
- Profit & Loss Insights

### 🤖 Stock Price Prediction
- Machine Learning-based Prediction
- Linear Regression Model
- Historical Price Analysis
- Next-Day Price Forecasting

### 📄 Report Generation
- Download Portfolio Reports
- Performance Summaries
- Investment Analysis Reports

### 👨‍💼 Admin Panel
- Manage Users
- View User Portfolios
- Monitor System Statistics
- Generate Reports

---

## 🛠️ Technology Stack

### Backend
- Python
- Flask
- Flask-Login
- Flask-MySQLdb
- Werkzeug Security

### Frontend
- HTML5
- CSS3
- Bootstrap 5

### Database
- MySQL

### Machine Learning
- Pandas
- NumPy
- Scikit-Learn

### Reporting
- ReportLab

---

## 📂 Project Structure

```text
StockWise/
│
├── app.py
├── config.py
├── requirements.txt
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── portfolio.html
│   ├── watchlist.html
│   ├── transactions.html
│   └── prediction.html
│
├── routes/
├── models/
├── services/
├── database/
├── reports/
└── ml/
```

---

## 🗄️ Database Schema

### Users
```sql
user_id
name
email
password
created_at
```

### Portfolio
```sql
portfolio_id
user_id
stock_symbol
company_name
quantity
buy_price
buy_date
```

### Watchlist
```sql
watchlist_id
user_id
stock_symbol
company_name
```

### Transactions
```sql
transaction_id
user_id
stock_symbol
transaction_type
quantity
price
transaction_date
```

### Admin
```sql
admin_id
username
password
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/kishoresrinivasan2005/Stockwise-stockmarket-portfolio-management.git
cd Stockwise-stockmarket-portfolio-management
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / Mac**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure MySQL Database

Create a MySQL database:

```sql
CREATE DATABASE stockwise;
```

Import the provided SQL schema.

Update database credentials inside:

```python
config.py
```

Example:

```python
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'stockwise'
```

### 5️⃣ Run Application

```bash
python app.py
```

Application will run on:

```text
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Dashboard
- Portfolio Overview
- Investment Statistics
- Profit/Loss Summary

### Portfolio Management
- Add Stocks
- Edit Holdings
- Delete Holdings

### Stock Prediction
- Historical Data Analysis
- Price Forecasting

*(Add screenshots here after deployment)*

---

## 🎯 Future Enhancements

- Real-Time Stock Market API Integration
- Live Price Tracking
- Portfolio Risk Analysis
- Email Notifications
- Dividend Tracking
- Advanced Machine Learning Models
- Interactive Charts and Visualizations
- Mobile Application Support

---

## 📚 Learning Outcomes

This project demonstrates:

- Full-Stack Web Development
- Flask Framework
- MySQL Database Design
- Authentication & Authorization
- CRUD Operations
- Machine Learning Integration
- Report Generation
- Responsive UI Design

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a Pull Request

---

## 📄 License

This project is developed for educational and portfolio purposes.

---

## 👨‍💻 Author

**Kishore Srinivasan**

GitHub: https://github.com/kishoresrinivasan2005

---

⭐ If you found this project useful, consider giving it a star!
