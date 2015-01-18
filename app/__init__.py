from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Load WTForms config from config.py
app.config.from_object('config')
db = SQLAlchemy(app)

# import after after app variable to prevent circular import
from app import views, models