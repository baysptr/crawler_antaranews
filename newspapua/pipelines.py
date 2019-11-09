# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class NewspapuaPipeline(object):
#     def process_item(self, item, spider):
#         return item

class NewspapuaPipeline(object):
	def __init__(self):
		import psycopg2
		self.conn = psycopg2.connect(
			user="megangs",
			dbname="newspapua",
			host='127.0.0.1:5432')

	def process_item(self, item, spider):
		cur = self.conn.cursor()
		cur.execute('''
			insert into papua ( link, title, author, created_at, body)
			values (%s, %s, %s, %s, %s);
			''', [
			item['link'], item['title'], item['author'], item['created_at'], item['body']
			])
		self.conn.commit()
		return item