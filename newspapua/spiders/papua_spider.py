import scrapy

class PapuaSpider(scrapy.Spider):
	name = "PapuaSpider"
	allowed_domains = ["papua.antaranews.com"]
	start_urls = ["https://papua.antaranews.com/berita"]

	def parse(self, response):
		for href in response.xpath('//div[@class="terkininew/div[@class="scroll-id ps-container ps-active-y"]/div[@class="ulx_terkininew"]/article[@class="simple-post clearfix"]/header/h3/a"]'):
			url = response.urljoin(href.extract_first())
			yield scrapy.Request(url, callback=self.parse_item)
		try:
			next_page = response.urljoin(response.xpath('//div[@class="post-content clearfix"]/nav/ul[@class="pagination pagination-sm"]/li/a').extract_first())
			yield scrapy.Request(next_page, callback=self.parse)
		except:
			pass

	def parse_news(self, response):
		link = response.url
		title = response.xpath('//header[@class="post-header"]/h1[@class="post-title"]/text()').extract()
		author = response.xpath('//footer[@class="post-meta"]/div[@class="tags-wrapper"]/span[@itemprop="author"]/text()').extract()
		created_at = response.xpath('//header[@class="post-header"]/p[@class="simple-here"]/span/span[@class="article-date"]/time/text()').extract()
		body = response.xpath('//div[@class="post-content clearfix font17"]/text()').extract()
		item = NewspapuaItem(
			link = link,
			title = title,
			author = author,
			created_at = created_at,
			body = body
			)
		return item