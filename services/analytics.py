import yfinance as yf
from models.portfolio import PortfolioItem
from models.transaction import Transaction

def get_current_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period='1d')
        if not data.empty:
            return float(data['Close'].iloc[-1])
    except Exception as e:
        print(f"Error fetching price for {symbol}: {e}")
    return 0.0

def calculate_dashboard_metrics(user_id):
    items = PortfolioItem.get_by_user(user_id)
    total_investment = 0.0
    current_value = 0.0
    num_stocks = len(items)
    best_stock = None
    best_profit = -float('inf')
    
    portfolio_data = []
    
    for item in items:
        invested = float(item['quantity'] * item['buy_price'])
        total_investment += invested
        
        current_price = get_current_price(item['stock_symbol'])
        if current_price == 0.0:
            current_price = float(item['buy_price'])
            
        value = float(item['quantity'] * current_price)
        current_value += value
        
        profit = value - invested
        if profit > best_profit:
            best_profit = profit
            best_stock = item['stock_symbol']
            
        portfolio_data.append({
            'symbol': item['stock_symbol'],
            'company': item['company_name'],
            'quantity': item['quantity'],
            'buy_price': float(item['buy_price']),
            'current_price': current_price,
            'invested': invested,
            'current_value': value,
            'profit': profit,
            'profit_pct': (profit / invested * 100) if invested > 0 else 0
        })
        
    total_profit = current_value - total_investment
    
    return {
        'total_investment': total_investment,
        'current_value': current_value,
        'total_profit': total_profit,
        'num_stocks': num_stocks,
        'best_stock': best_stock if num_stocks > 0 else 'N/A',
        'portfolio_data': portfolio_data
    }

def calculate_analytics(user_id):
    metrics = calculate_dashboard_metrics(user_id)
    
    allocation = []
    if metrics['current_value'] > 0:
        for p in metrics['portfolio_data']:
            pct = (p['current_value'] / metrics['current_value']) * 100
            allocation.append({
                'symbol': p['symbol'],
                'percentage': pct,
                'value': p['current_value']
            })
            
    transactions = Transaction.get_by_user(user_id)
    monthly_investment = {}
    for t in transactions:
        if t['transaction_type'] == 'BUY':
            month = t['transaction_date'].strftime('%Y-%m')
            val = float(t['quantity'] * t['price'])
            monthly_investment[month] = monthly_investment.get(month, 0) + val
            
    sorted_months = sorted(monthly_investment.keys())
    monthly_data = [{'month': m, 'invested': monthly_investment[m]} for m in sorted_months]
    
    metrics['allocation'] = sorted(allocation, key=lambda x: x['percentage'], reverse=True)
    metrics['monthly_data'] = monthly_data
    
    return metrics
