# -*- coding: utf-8 -*-

from flask import abort, url_for, redirect, request
from homeland import app
from flask.ext.mako import render_template

@app.route("/add_link", methods=['GET', 'POST'])
def add_link():
    if request.method == 'POST':
        url = request.form['link']
        from homeland.utils.crawl_douban import crawl_douban
        res = crawl_douban(url)
        return render_template('add_link.html', res=res)
    else:
        return render_template('add_link.html')
