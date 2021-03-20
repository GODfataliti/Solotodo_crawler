# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy import signals
from scrapy.exceptions import DropItem
from scrapy import Request
import sqlite3


class SolotodoPipeline:
	def process_item(self, item, spider):
		return item

class NotebooksPipeline(object):

	def __init__(self):
		self.connection = sqlite3.connect('notebookdata.db')
		self.cursor = self.connection.cursor()
		self.cursor.execute('''
			CREATE TABLE IF NOT EXISTS NOTEBOOKS(
			ID_NOTEBOOK INTEGER PRIMARY KEY AUTOINCREMENT,
			TITULO VARCHAR(100),
			PRECIO VARCHAR(60),
			RAM VARCHAR(60),
			TARJ_VIDEO VARCHAR(60),
			PROCESADOR VARCHAR(60),
			ALMACENAMIENTO VARCHAR(60),
			URL VARCHAR(120))
		''')

	def process_item(self, item, spider):
		self.cursor.execute('SELECT * FROM NOTEBOOKS WHERE URL=?', item['url'])
		result = self.cursor.fetchone()
		if result:
			print(f"Item in db: {item['titulo']}")
		else:
			self.cursor.execute(
				"INSERT INTO NOTEBOOKS VALUES (NULL,?,?,?,?,?,?,?)",
				(item['titulo'][0],item['precio'][0],item['ram'][0],item['tarj_video'][0],
				item['procesador'][0],item['almacenamiento'][0],item['url'][0]))

			self.connection.commit()
			return item