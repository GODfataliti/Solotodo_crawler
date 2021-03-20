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

import sqlite3	# pip install pysqlite3


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
			PRECIO VARCHAR(60) NULL,
			RAM VARCHAR(60) NULL,
			TARJ_VIDEO VARCHAR(60) NULL,
			PROCESADOR VARCHAR(90) NULL,
			ALMACENAMIENTO VARCHAR(60) NULL,
			URL VARCHAR(120))
		''')

	def process_item(self, item, spider):
		self.cursor.execute("SELECT * FROM NOTEBOOKS WHERE URL=?", (item['url'],))
		result = self.cursor.fetchone()
		if result:
			print(f"Item in db: {item['titulo']}")
		else:
			data_item = (item['titulo'],item['precio'],item['ram'],item['tarj_video'],
				item['procesador'],item['almacenamiento'],item['url'])
			self.cursor.execute(
				"INSERT INTO NOTEBOOKS VALUES (NULL,?,?,?,?,?,?,?)", data_item)

			self.connection.commit()
		return item