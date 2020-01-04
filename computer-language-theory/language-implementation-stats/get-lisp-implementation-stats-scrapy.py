import scrapy


class CommonlispImplementationsSpider(scrapy.Spider):
    name = 'commonlisp_implementations'
    start_urls = [
        'https://en.wikipedia.org/wiki/Common_Lisp'
    ]

    def parse(self, response):
        table = response.css('table.infobox').css('tbody')
        print(table)
        for row in table.css('tr'):
            print(row.css('th'))
            print(row.css('th').get())

        # for in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').get(),
        #         'author': quote.xpath('span/small/text()').get(),
        #     }

        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
