from flask import Flask 
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from webdata.config import Config

config = Config()

app = Flask(__name__)

app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
app.config['PERMANENT_SESSION_LIFETIME'] = config.SESSION_LIFETIME

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
auth = LoginManager(app)

auth.login_view = 'main.login'
auth.login_message = 'Please login to proceed!'
auth.login_message_category = 'warning'

from webdata.main.routes import main
from webdata.user.routes import user
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(main, url_prefix='/')
