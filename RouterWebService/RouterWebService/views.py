"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from RouterWebService import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/admin')
def contact():
    return render_template(
        'admin.html',
        title='admin',
        year=datetime.now().year,
    )

@app.route('/dhcp')
def about():
    return render_template(
        'dhcp.html',
        title='dhcp',
        year=datetime.now().year,
    )
