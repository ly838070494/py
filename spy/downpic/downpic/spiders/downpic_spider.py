import scrapy
from downpic.items import DownpicItem

class DownpicSpider(scrapy.Spider):
	name = 'downpic'
	allowed_domains = ['win4000.com']
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
		'Host':'www.win4000.com'
	}

	start_urls = ['http://www.win4000.com/meitu.html']

	def parse(self, response):
		item = DownpicItem()
		p_list = response.xpath('//div[@class="tab_box"]/*/ul[@class="clearfix"]/li/a')
		for li in p_list:
			item['title'] = li.xpath('p/text()').extract()
			item['link'] = li.xpath('img/@data-original').extract()
		
			yield item