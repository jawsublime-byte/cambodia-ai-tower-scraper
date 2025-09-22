import scrapy
from googletrans import Translator

translator = Translator()

class Khmer24Spider(scrapy.Spider):
    name = "khmer24"
    allowed_domains = ["khmer24.com"]
    start_urls = [
        "https://www.khmer24.com/en/search?query=xeon",
        "https://www.khmer24.com/en/search?query=1660+ti",
        "https://www.khmer24.com/en/search?query=workstation"
    ]

    def parse(self, response):
        for item in response.css('.search-result-item'):
            title = item.css('.title::text').get()
            price = item.css('.price span::text').get()
            link = item.css('a::attr(href)').get()
            # Translate title and price if in Khmer
            title_en = translator.translate(title, src='km', dest='en').text if title else ""
            price_en = translator.translate(price, src='km', dest='en').text if price else ""
            yield {
                'title': title,
                'title_en': title_en,
                'price': price,
                'price_en': price_en,
                'link': response.urljoin(link)
            }
