from flask import Blueprint, render_template
from flask_login import login_required, current_user
from services.analytics import calculate_analytics

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/analytics')
@login_required
def index():
    metrics = calculate_analytics(current_user.user_id)
    return render_template('analytics.html', metrics=metrics)
