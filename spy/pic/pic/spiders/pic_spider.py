import scrapy

class PicSpider(scrapy.Spider):
	name = 'pic'
	allowed_domains = ['win4000.com']
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
		'Host':'www.win4000.com'
	}

	def start_requests(self):
		urls = [
			'http://www.win4000.com/meinv153280.html',
			'http://www.win4000.com/meinv151812.html'
		]
		for url in urls:
			yield scrapy.Request(url=url,headers=self.headers, callback=self.parse)

	def parse(self, response):
		filename = response.url.split("/")[-1]
		with open(filename, 'wb') as f:
			f.write(response.body)