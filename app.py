from flask import Flask
from flask_login import LoginManager
from views import views
from models import User
import shelve

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.register_blueprint(views, url_prefix='/')


login_manager = LoginManager(app)
login_manager.login_view = 'views.login'


DATABASE_FILE = "database.db"


@login_manager.user_loader
def load_user(user_id):
    try:
        with shelve.open(DATABASE_FILE) as db:
            user_data = db.get(user_id)
            if user_data:
                return User(user_id, user_data['username'], user_data['password'])
    except (EOFError, KeyError, TypeError):

        pass
    return None

if __name__ == "__main__":
    app.run(debug=True)
