from flask import Blueprint, render_template, request
from flask_login import login_required
from ml.predictor import predict_stock_price

ml_bp = Blueprint('ml', __name__)

@ml_bp.route('/prediction', methods=['GET', 'POST'])
@login_required
def index():
    prediction_data = None
    error = None
    
    if request.method == 'POST':
        symbol = request.form.get('symbol').upper()
        prediction_data, error = predict_stock_price(symbol)
        
    return render_template('prediction.html', prediction=prediction_data, error=error)
