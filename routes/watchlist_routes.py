from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.watchlist import WatchlistItem

watchlist_bp = Blueprint('watchlist', __name__)

@watchlist_bp.route('/watchlist')
@login_required
def index():
    items = WatchlistItem.get_by_user(current_user.user_id)
    return render_template('watchlist.html', items=items)

@watchlist_bp.route('/watchlist/add', methods=['POST'])
@login_required
def add():
    stock_symbol = request.form.get('stock_symbol').upper()
    company_name = request.form.get('company_name')
    
    if WatchlistItem.add(current_user.user_id, stock_symbol, company_name):
        flash(f'{stock_symbol} added to watchlist.', 'success')
    else:
        flash(f'{stock_symbol} is already in your watchlist.', 'warning')
        
    return redirect(url_for('watchlist.index'))

@watchlist_bp.route('/watchlist/remove/<int:watchlist_id>', methods=['POST'])
@login_required
def remove(watchlist_id):
    WatchlistItem.delete(watchlist_id, current_user.user_id)
    flash('Stock removed from watchlist.', 'info')
    return redirect(url_for('watchlist.index'))
