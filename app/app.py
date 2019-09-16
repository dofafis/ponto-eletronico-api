from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('../config/DevelopmentConfig.py')
db = SQLAlchemy(app)
db.init_app(app)
