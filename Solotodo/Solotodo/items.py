# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


class SolotodoItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = Field()
    precio = Field()
    ram = Field()
    tarj_video = Field()
    procesador = Field()
    almacenamiento = Field()
    url = Field()

    pass
