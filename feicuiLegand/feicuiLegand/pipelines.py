# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from feicuiLegand.db.dbHelper import DBHelper
class FeicuilegandPipeline(object):
    def process_item(self, item, spider):
        return item


class FeicuiXinpinPipeline(object):
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        # 插入数据库
        self.db.insert(item)
        return item


class FeicuiSuggestPipeline(object):
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        # 插入数据库
        self.db.insert(item)
        return item