# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class DownpicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
    	for url in item['link']:
    		if re.match(r'^http://.*$', url):
    			yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok,x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['link'] = image_path
        return item