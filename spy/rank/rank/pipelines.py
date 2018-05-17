# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import re

class RankPipeline(object):

    def process_item(self, item, spider):
    	title = item['title']
    	title = '_'.join(re.findall('([a-zA-Z]+)', title))
    	content = item['content']
    	with open(r'C:/python/file/{}.json'.format(title), 'w') as f:
    		f.write(json.dumps(content))
    	return item
        
