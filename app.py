from flask import Flask, render_template
from config import Config
import db
from flask_login import LoginManager
from models.user import User, Admin

login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # Configure user loader
    @login_manager.user_loader
    def load_user(user_id):
        if user_id.startswith('admin_'):
            admin_id = user_id.split('_')[1]
            return Admin.get(admin_id)
        return User.get(user_id)

    # Register blueprints
    from routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)
    
    from routes.portfolio_routes import portfolio_bp
    app.register_blueprint(portfolio_bp)
    
    from routes.watchlist_routes import watchlist_bp
    app.register_blueprint(watchlist_bp)
    
    from routes.transactions_routes import transactions_bp
    app.register_blueprint(transactions_bp)
    
    from routes.analytics_routes import analytics_bp
    app.register_blueprint(analytics_bp)
    
    from routes.admin_routes import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    from routes.ml_routes import ml_bp
    app.register_blueprint(ml_bp)
    
    from routes.reports_routes import reports_bp
    app.register_blueprint(reports_bp)

    @app.route('/')
    def index():
        from flask_login import current_user
        from flask import redirect, url_for
        if current_user.is_authenticated:
            if getattr(current_user, 'id', '').startswith('admin_'):
                # return redirect(url_for('admin.dashboard'))
                pass
            return redirect(url_for('portfolio.dashboard'))
        return render_template('home.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
