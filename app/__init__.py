from flask import Flask

app = Flask(__name__)
# Load WTForms config from config.py
app.config.from_object('config')

# import after after app variable to prevent circular import
from app import views

