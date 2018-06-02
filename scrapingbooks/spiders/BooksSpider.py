import scrapy
from scrapingbooks.items import ScrapingbooksItem


class BooksSpider(scrapy.Spider):
    name = "bookspider"
    filename = 'books.txt'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/category/books_1/page-1.html']
    file = open(filename, 'w')

    def start_requests(self):
        url = self.start_urls[0]
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for book in response.css('div.image_container'):
            item = ScrapingbooksItem()
            book_name = str(book.css('img::attr(alt)').extract_first().encode('ascii', 'ignore'))
            item['name'] = book_name
            yield {
                'name': book_name
                }

            self.file.write(book_name + '\n')

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
