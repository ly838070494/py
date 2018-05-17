import scrapy
from top250.items import Top250Item
#from scrapy.shell import inspect_response 调试

class Top250Spider(scrapy.Spider):
	name = 'top250'
	allowed_domains = ['movie.douban.com']
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
	}
	url = 'https://movie.douban.com/top250'

	def start_requests(self):
		yield scrapy.Request(url=self.url, headers=self.headers)

	def parse(self, response):
		#inspect_response(response, self) 命令行调试
		movies = response.xpath('//ol[@class="grid_view"]/li')
		item = Top250Item()
		for movie in movies:
			item['rank'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()
			item['name'] = movie.xpath('.//div[@class="info"]/div[@class="hd"]/a/span[1]/text()').extract()
			item['score'] = movie.xpath('.//div[@class="star"]/span[2]/text()').extract()
			item['num'] = movie.xpath('.//div[@class="star"]/span[4]/text()').re('(\d+)人评价')

			yield item
		next_url = response.xpath('//span[@class="next"]/a/@href').extract()
		if next_url:
			next_url = self.url + next_url[0]
			yield scrapy.Request(next_url, headers=self.headers)


