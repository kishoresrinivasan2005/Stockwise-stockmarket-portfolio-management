from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from models.user import Admin, User
from db import get_db

admin_bp = Blueprint('admin', __name__)

def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not getattr(current_user, 'id', '').startswith('admin_'):
            flash('Admin access required.', 'danger')
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated and getattr(current_user, 'id', '').startswith('admin_'):
        return redirect(url_for('admin.dashboard'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        admin_user = Admin.find_by_username(username)
        if admin_user and check_password_hash(admin_user.password, password):
            login_user(admin_user)
            return redirect(url_for('admin.dashboard'))
            
        flash('Invalid admin credentials.', 'danger')
        
    return render_template('admin/login.html')

@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) as count FROM users")
    total_users = cursor.fetchone()['count']
    
    cursor.execute("SELECT COUNT(*) as count FROM portfolio")
    total_portfolios = cursor.fetchone()['count']
    
    cursor.execute("SELECT COUNT(*) as count FROM transactions")
    total_transactions = cursor.fetchone()['count']
    cursor.close()
    
    stats = {
        'total_users': total_users,
        'total_portfolios': total_portfolios,
        'total_transactions': total_transactions
    }
    return render_template('admin/dashboard.html', stats=stats)

@admin_bp.route('/users')
@admin_required
def users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users ORDER BY created_at DESC")
    all_users = cursor.fetchall()
    cursor.close()
    return render_template('admin/users.html', users=all_users)

@admin_bp.route('/users/delete/<int:user_id>', methods=['POST'])
@admin_required
def delete_user(user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    db.commit()
    cursor.close()
    flash('User deleted successfully.', 'success')
    return redirect(url_for('admin.users'))

@admin_bp.route('/portfolios')
@admin_required
def portfolios():
    db = get_db()
    cursor = db.cursor()
    query = """
        SELECT p.*, u.name as user_name, u.email 
        FROM portfolio p
        JOIN users u ON p.user_id = u.user_id
        ORDER BY p.buy_date DESC
    """
    cursor.execute(query)
    all_portfolios = cursor.fetchall()
    cursor.close()
    return render_template('admin/portfolios.html', portfolios=all_portfolios)

