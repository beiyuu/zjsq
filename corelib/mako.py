from flask import g
from flask.ext.mako import MakoTemplates
from homeland import app

mako_import = ['from homeland.utils.mako_filters import collect_js, collect_css']
app.config['MAKO_IMPORTS'] = mako_import
mako = MakoTemplates(app)

@app.after_request
def add_collect_js_css(response):
    content_type = response.headers.get('content-type', '')
    if content_type == 'text/html; charset=utf-8':
        output = response.data
        js_holder = '<!-- COLLECTED JS -->'
        js_data = inline_block('js')
        if js_data and js_holder in output:
            output = output.replace(js_holder, js_data, 1)

        css_holder = '<!-- COLLECTED CSS -->'
        css_data = inline_block('css')
        if css_data and css_holder in output:
            output = output.replace(css_holder, css_data, 1)
        response.data = output
    return response

def inline_block(block_type):
    g_items = g.get('mako_collected_items', None)
    if not g_items:
        return None

    contents = g_items.get(block_type)
    if not contents:
        return ''
    content = ''.join(contents)
    if block_type == 'js':
        return '<script type="text/javascript">%s</script>' % content
    elif block_type == 'css':
        return '<style type="text/css">%s</style>' % content
