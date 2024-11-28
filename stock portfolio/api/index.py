from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is Flask running on Vercel!'

# Add more routes for your stock data and other functionalities here

# This is the WSGI entry point required by Vercel for Flask apps.
def handler(request):
    with app.app_context():
        return app.full_dispatch_request()

# Vercel will use this handler for all incoming requests
