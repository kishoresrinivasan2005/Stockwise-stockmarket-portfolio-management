from flask import Blueprint, send_file, redirect, url_for, flash
from flask_login import login_required, current_user
from reports.generator import generate_portfolio_pdf

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/reports/download')
@login_required
def download():
    try:
        pdf_buffer = generate_portfolio_pdf(current_user.user_id)
        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name=f'StockWise_Report_{current_user.name}.pdf',
            mimetype='application/pdf'
        )
    except Exception as e:
        flash(f'Error generating report: {str(e)}', 'danger')
        return redirect(url_for('portfolio.dashboard'))
