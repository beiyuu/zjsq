# -*- coding: utf-8 -*-
from homeland.corelib.mongo import mongo
from bson.objectid import ObjectId

class TV():
    def __init__(self, id):
        tv = mongo.db.tv_show.find_one({'_id':ObjectId(id)})
        self.id = id
        self.url_name = tv['url_name']
        self.cn_name = tv['cn_name']
        self.origin_name = tv['origin_name']
        self.aka_name = tv['aka_name']
        self.directors = tv['directors']
        self.casts = tv['casts']
        self.writers = tv['writers']
        self.languages = tv['languages']
        self.countries = tv['countries']
        self.summary = tv['summary']
        self.is_ended = tv['is_ended']

    @property
    def cn_name(self):
        return self.cn_name

    @property
    def url_name(self):
        return self.url_name

    @property
    def origin_name(self):
        return self.origin_name

    @property
    def aka_name(self):
        return self.aka_name

    @property
    def directors(self):
        return self.directors

    @property
    def casts(self):
        return self.casts

    @property
    def writers(self):
        return self.writers

    @property
    def languages(self):
        return self.languages

    @property
    def countries(self):
        return self.countries

    @property
    def summary(self):
        return self.summary

    @property
    def is_ended(self):
        return self.is_ended

    @classmethod
    def get(cls, url_name):
        if not url_name:
            return None
        tv = mongo.db.tv_show.find_one({'url_name': url_name})
        return cls(tv['_id']) if tv else None

    @classmethod
    def addTV(cls, cn_name, url_name, origin_name, aka_name, directors,
            casts, writers, languages, countries, summary, is_ended):

        mongo.db.tv_show.insert({
            'cn_name': cn_name,
            'url_name': url_name,
            'origin_name': origin_name,
            'aka_name': aka_name,
            'directors': directors,
            'casts': casts,
            'writers': writers,
            'languages': languages,
            'countries': countries,
            'summary': summary,
            'is_ended': is_ended
        })

    @classmethod
    def updateTV(cls, cn_name, url_name, origin_name, aka_name, directors,
            casts, writers, languages, countries, summary, is_ended):

        mongo.db.tv_show.update(
                {'url_name': url_name},
                {'$set': {
                    'cn_name': cn_name,
                    'origin_name': origin_name,
                    'aka_name': aka_name,
                    'directors': directors,
                    'casts': casts,
                    'writers': writers,
                    'languages': languages,
                    'countries': countries,
                    'summary': summary,
                    'is_ended': is_ended
                    }
                }
        )
