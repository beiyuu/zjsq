# -*- coding: utf-8 -*-

import requests
import re
from pyquery import PyQuery as pq
from urlparse import urlparse
from homeland.corelib.mongo import mongo

def crawl_douban(url):
    tid = get_link_id(url)
    res = {}
    if not tid:
        res['error'] = '请填写正确的URL'
        return res
    else:
        res = is_exist(tid)
        if not res:
            res = {}
            r = requests.get(url, timeout=10)
            if(r.status_code == 200):
                p = pq(r.text)
                title = p('h1').text()
                is_tv = 1 if p('input[name=tv_id]').val() else 0

                res['title'] = title
                res['is_tv'] = is_tv
                mongo.db.douban_movie_id.insert({'douban_id':tid,
                                                 'title':title,
                                                 'is_tv':is_tv})
    return res

def get_link_id(url):
    re_movie = "http://movie(\..*)?.douban.com/subject/(\d+)"
    match = re.compile(re_movie).match(url)
    return match.groups()[1] if match else None

def is_exist(eid):
    eid = mongo.db.douban_movie_id.find_one({'douban_id':eid})
    res = {}
    if eid:
        res['title'] =  eid['title']
        res['is_tv'] = eid['is_tv']
    return res if eid else None
