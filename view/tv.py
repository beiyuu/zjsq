from flask import abort, url_for, redirect
from homeland import app
from homeland.model.tv import TV
from flask.ext.mako import render_template

@app.route('/<uname>/')
def tvname(uname):
    tv = TV.get(uname)
    if tv:
        return 'tv %s' % tv.name
    else:
        abort(404)
