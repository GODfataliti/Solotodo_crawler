#FOR THIS PROJECT WILL USE SCRAPY - YOU CAN INSTALL LIKE ANY PACKAGE USEING PIP INSTALL SCRAPY.

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from Solotodo.items import SolotodoItem

#GLOBAL VAR
URL = 'https://www.solotodo.cl/notebooks?score_games_start=440'
DOMAIN = 'https://www.solotodo.cl/'


class SolotodoSpider(CrawlSpider):
	name='solotodo'


	allowed_domain = [DOMAIN]
	start_urls=[URL]

	item_count = 0
	rules = {
	#Para cada item
		Rule(LinkExtractor(allow=(), restrict_xpaths=('//ul[@class="pagination"]/li/a[text()="Siguiente"]'))), #Siguiente
		Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@id="category-browse-results-card"]/div/div[2]/div/div/h3')), #Ingresar al producto
			callback='parse_item', follow=False)
	}

	def parse_item(self, response):

		db_item = SolotodoItem()

		db_item['titulo'] = response.xpath('normalize-space(//div/h1[@class="mb-0"]/text())').get()
		db_item['precio'] = response.xpath('normalize-space(//div[@id="product-prices-table"]/table/tbody/tr[1]/td[4]//text())').get()
		db_item['ram'] = response.xpath('normalize-space(//div[@id="technical-specifications-container"]/div/div[1]/dl/dd[2]//text())').get()
		db_item['tarj_video'] = response.xpath('normalize-space(//div[@id="technical-specifications-container"]/div/div[1]/dl/dd[6]//text())').get()
		db_item['procesador'] = response.xpath('normalize-space(//div[@id="technical-specifications-container"]/div/div[1]/dl/dd[1]/a//text())').get()
		db_item['almacenamiento'] = response.xpath('normalize-space(//div[@id="technical-specifications-container"]/div/div[1]/dl/dd[5]//text())').get()
		db_item['url'] = response.url

		self.item_count+=1

		if self.item_count>10:
			raise CloseSpider('item_exceeded')

		yield db_item