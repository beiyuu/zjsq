# -*- coding: utf-8 -*-
from homeland.corelib.mongo import mongo
from bson.objectid import ObjectId

class TV():
    def __init__(self, id):
        tv = mongo.db.tv_show.find_one({'_id':ObjectId(id)})
        self.id = id
        self.name= tv['name']
        self.cname= tv['cname']

    @property
    def name(self):
        """Get the tv cnname."""
        return self.nname

    @property
    def cname(self):
        """Get the tv cnname."""
        return self.cnname

    @classmethod
    def get(cls, url_name):
        if not url_name:
            return None
        tv = mongo.db.tv_show.find_one({'$or': [{'url_name': url_name}]})
        return cls(tv['_id']) if tv else None

    def getAllEpi(self):
        pass

    def getEpi(self):
        pass

    def editEpi(self):
        pass

    def addEpi(self):
        pass

    @classmethod
    def addTV(cls, cn_name, url_name, origin_name, aka_name, directors,
            casts, writers, languages, countries, summary, is_ended):

        mongo.db.tv_show.insert({
            'cn_name': cn_name,
            'url_name': url_name,
            'origin_name': origin_name,
            'aka_name': aka_name,
            'casts': casts,
            'writers': writers,
            'languages': languages,
            'countries': countries,
            'summary': summary,
            'is_ended': is_ended
        })
