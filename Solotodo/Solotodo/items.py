# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SolotodoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    precio = scrapy.Field()
    ram = scrapy.Field()
    tarj_video = scrapy.Field()
    procesador = scrapy.Field()
    almacenamiento = scrapy.Field()
    url = scrapy.Field()

    pass
