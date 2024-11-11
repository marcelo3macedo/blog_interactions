"""
Flask configs and initialization
"""
import os
from flask import Flask
from app.cache_config import cache
from app.routes import main
from app.models import db

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = (
  f"mysql+pymysql://{os.getenv('MYSQL_USER')}:"
  f"{os.getenv('MYSQL_PASSWORD')}@"
  f"{os.getenv('MYSQL_HOST')}/"
  f"{os.getenv('MYSQL_DB')}"
)

app.config['CACHE_TYPE'] = 'simple'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300
cache.init_app(app)

app.register_blueprint(main)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
