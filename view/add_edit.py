# -*- coding: utf-8 -*-
from flask import abort, request
from homeland import app
from homeland.model.tv import TV
from flask.ext.mako import render_template

def list_item(form, item_name):
    ret = form.getlist(item_name)
    ret = [x.strip() for x in ret]
    ret = [x for x in ret if x]
    return ret

@app.route('/add/', methods=['GET', 'POST'])
def add_tv():
    edit_tv = False
    if request.method == 'POST':
        form = request.form
        cn_name = form.get('cn_name').strip()
        url_name = form.get('url_name').strip()
        origin_name = form.get('origin_name').strip()
        aka_name = list_item(form, 'aka_name')
        directors = list_item(form, 'directors')
        casts = list_item(form, 'casts')
        writers = list_item(form, 'writers')
        languages = list_item(form, 'languages')
        countries = list_item(form, 'countries')
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

@app.route('/<url_name>/edit/', methods=['GET', 'POST'])
def edit_tv(url_name):
    tv = TV.get(url_name)
    edit_tv = True
    eidt_succ = False

    if request.method == 'POST':
        form = request.form
        cn_name = form.get('cn_name').strip()
        origin_name = form.get('origin_name').strip()
        aka_name = list_item(form, 'aka_name')
        directors = list_item(form, 'directors')
        casts = list_item(form, 'casts')
        writers = list_item(form, 'writers')
        languages = list_item(form, 'languages')
        countries = list_item(form, 'countries')
        summary = form.get('summary').strip()
        is_ended = int(form.get('is_ended', 0))

        if not cn_name:
            error = '请填写剧集中文名称'
            return render_template('add_edit.html', **locals())

        TV.updateTV(cn_name=cn_name, url_name=url_name, origin_name=origin_name,
                aka_name=aka_name, directors=directors, casts=casts, writers=writers,
                languages=languages, countries=countries, summary=summary,
                is_ended=is_ended)
        edit_succ = True
        return render_template('add_edit.html', **locals())

    if tv:
        cn_name = tv.cn_name
        url_name = tv.url_name
        origin_name = tv.origin_name
        aka_name = tv.aka_name
        directors = tv.directors
        casts = tv.casts
        writers = tv.writers
        languages = tv.languages
        countries = tv.countries
        summary = tv.summary
        is_ended = tv.is_ended
        return render_template('add_edit.html', **locals())
    else:
        abort(404)
