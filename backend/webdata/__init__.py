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
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
app.config['ALLOWED_FILE'] = config.ALLOWED_FILE
app.config['FOLDER_NAME'] = config.FOLDER_NAME

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
auth = LoginManager(app)


auth.login_view = 'main.login'
auth.login_message = 'Please login to proceed!'
auth.login_message_category = 'warning'

from webdata.main.routes import main
from webdata.user.routes import user
from webdata.redeem.routes import redeem
from webdata.dashboard.routes import dashboard
from webdata.penjemputan.routes import penjemputan
from webdata.rekomendasi.routes import rekomendasi
from webdata.artikel.routes import artikel
app.register_blueprint(artikel, url_prefix='/artikel')
app.register_blueprint(rekomendasi, url_prefix='/rekomendasi')
app.register_blueprint(penjemputan, url_prefix='/penjemputan')
app.register_blueprint(dashboard, url_prefix='/dashboard')
app.register_blueprint(redeem, url_prefix='/redeem')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(main, url_prefix='/')
