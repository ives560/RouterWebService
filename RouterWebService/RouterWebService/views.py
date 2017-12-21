# -*- coding: utf8 -*-
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from RouterWebService import app

import network

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    """中文"""
    net = network.network()
    interfaces = net.GetInterfaces()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        interface = interfaces['\xd2\xd4\xcc\xab\xcd\xf8'],
    )

@app.route('/admin')
def admin():
    return render_template(
        'admin.html',
        title='admin',
        year=datetime.now().year,
    )

@app.route('/dhcp')
def dhcp():
    return render_template(
        'dhcp.html',
        title='dhcp',
        year=datetime.now().year,
    )


@app.route('/webconsole')
def webconsole():
    return render_template(
        'webconsole.html',
    )