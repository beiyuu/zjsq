from flask.ext.mako import render_template
from homeland import app

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
