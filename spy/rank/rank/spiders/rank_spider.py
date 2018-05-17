from scrapy import Spider, Request
from rank.items import RankItem
import logging
from scrapy.shell import inspect_response

class RankSpider(Spider):
	name = 'rank'
	allowed_domains = ['ranking.promisingedu.com']
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
	}
	url = 'http://ranking.promisingedu.com/major/qs'
	def start_requests(self):
		yield Request(url=self.url,headers=self.headers,callback=self.parse)

	def parse(self, response):
		#inspect_response(response, self)
		links = response.xpath('//table[@class="rank-list"]/tr/td')
		logging.info('info:')
		for link in links:
			name = link.xpath('.//a/text()').extract()
			href = link.xpath('.//a/@href').extract()
			logging.info('href:%s' % href[0])
			if href:
				yield Request(href[0], meta={'name':name}, callback=self.parse_major)

	def parse_major(self, response):
		# inspect_response(response, self)
		tds = response.xpath('//table[@class="rank-items"]/tbody/tr')
		item = RankItem()
		item['title'] = response.meta['name'][0]
		item['content'] = []
		data = {}
		for td in tds:
			data['Ranking'] = td.xpath('.//td[1]/text()').extract_first()
			data['University_Name'] = td.xpath('.//td[2]/text()').extract_first()
			data['Region'] = td.xpath('.//td[3]/text()').extract_first()
			data['Academic_Reputation'] = td.xpath('.//td[4]/text()').extract_first()
			data['Employer_Reputation'] = td.xpath('.//td[5]/text()').extract_first()
			data['Citations_per_Pape'] = td.xpath('.//td[6]/text()').extract_first()
			data['H_index_Citations'] = td.xpath('.//td[7]/text()').extract_first()
			data['Overall_score'] = td.xpath('.//td[8]/text()').extract_first()
			
			item['content'].append(data)
		
		yield item

