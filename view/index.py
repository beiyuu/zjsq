# -*- coding: utf-8 -*-

from flask import render_template, abort, url_for, redirect
from homeland import app
from homeland.model.tv import TV
from flask.ext.mako import render_template

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/user/')
def username():
    return 'User %s' % url_for('username')
