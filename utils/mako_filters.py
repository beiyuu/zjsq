# -*- coding: UTF-8 -*-

def mako_collect(name):
    '''
    把渲染出来的html暂存在一个数组中，统一输出
    '''
    def _(content):
        from flask import g
        items = g.get('mako_collected_items', None)
        if items is None:
            items = g.mako_collected_items = {}
        items.setdefault(name, []).append(content)
        return ''
    return _

collect_js = mako_collect('js')
collect_css = mako_collect('css')
