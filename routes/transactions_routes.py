from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.transaction import Transaction

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/transactions')
@login_required
def index():
    items = Transaction.get_by_user(current_user.user_id)
    return render_template('transactions.html', items=items)
