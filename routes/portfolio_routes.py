from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.portfolio import PortfolioItem
from models.transaction import Transaction
from services.analytics import calculate_dashboard_metrics
from datetime import datetime

portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.route('/dashboard')
@login_required
def dashboard():
    metrics = calculate_dashboard_metrics(current_user.user_id)
    return render_template('dashboard.html', metrics=metrics)

@portfolio_bp.route('/portfolio')
@login_required
def index():
    items = PortfolioItem.get_by_user(current_user.user_id)
    return render_template('portfolio/index.html', items=items)

@portfolio_bp.route('/portfolio/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        stock_symbol = request.form.get('stock_symbol').upper()
        company_name = request.form.get('company_name')
        quantity = int(request.form.get('quantity'))
        buy_price = float(request.form.get('buy_price'))
        buy_date = request.form.get('buy_date')

        PortfolioItem.add(current_user.user_id, stock_symbol, company_name, quantity, buy_price, buy_date)
        Transaction.add(current_user.user_id, stock_symbol, 'BUY', quantity, buy_price)
        
        flash('Stock added successfully!', 'success')
        return redirect(url_for('portfolio.index'))
        
    return render_template('portfolio/add.html')

@portfolio_bp.route('/portfolio/edit/<int:portfolio_id>', methods=['GET', 'POST'])
@login_required
def edit(portfolio_id):
    item = PortfolioItem.get_by_id(portfolio_id, current_user.user_id)
    if not item:
        flash('Stock not found.', 'danger')
        return redirect(url_for('portfolio.index'))
        
    if request.method == 'POST':
        quantity = int(request.form.get('quantity'))
        buy_price = float(request.form.get('buy_price'))
        buy_date = request.form.get('buy_date')
        
        PortfolioItem.update(portfolio_id, current_user.user_id, quantity, buy_price, buy_date)
        flash('Stock updated successfully!', 'success')
        return redirect(url_for('portfolio.index'))
        
    return render_template('portfolio/edit.html', item=item)

@portfolio_bp.route('/portfolio/delete/<int:portfolio_id>', methods=['POST'])
@login_required
def delete(portfolio_id):
    item = PortfolioItem.get_by_id(portfolio_id, current_user.user_id)
    if item:
        PortfolioItem.delete(portfolio_id, current_user.user_id)
        flash('Stock removed from portfolio.', 'info')
    return redirect(url_for('portfolio.index'))
