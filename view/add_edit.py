# -*- coding: utf-8 -*-
from flask import abort, request
from homeland import app
from homeland.model.tv import TV
from flask.ext.mako import render_template

@app.route('/add/', methods=['GET', 'POST'])
def add_tv():
    if request.method == 'POST':
        def list_item(item_name):
            ret = form.getlist(item_name)
            ret = [x.strip() for x in ret]
            ret = [x for x in ret if x]
            return ret

        form = request.form
        cn_name = form.get('cn_name').strip()
        url_name = form.get('url_name').strip()
        origin_name = form.get('origin_name').strip()
        aka_name = list_item('aka_name')
        directors = list_item('directors')
        casts = list_item('casts')
        writers = list_item('writers')
        languages = list_item('languages')
        countries = list_item('countries')
        summary = form.get('summary').strip()
        is_ended = int(form.get('is_ended', 0))

        if not cn_name:
            error = '请填写剧集中文名称'
            return render_template('add_edit.html', **locals())
        if not url_name:
            error = '请填写剧集唯一URL'
            return render_template('add_edit.html', **locals())

        TV.addTV(cn_name=cn_name, url_name=url_name, origin_name=origin_name,
                aka_name=aka_name, directors=directors, casts=casts, writers=writers,
                languages=languages, countries=countries, summary=summary,
                is_ended=is_ended)

        return render_template('add_succ.html', **locals())

    return render_template('add_edit.html', **locals())

@app.route('/edit/<url_name>')
def edit_tv(url_nme):
    return render_template('add_edit.html')
