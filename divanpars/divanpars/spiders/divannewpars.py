import scrapy


class LightingSpider(scrapy.Spider):
    name = "lightingspider"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/stavropol/category/svet"]

    def parse(self, response):
        lightings = response.css('div._Ud0k')  # Проверьте и замените селектор, если он изменится
        for lighting in lightings:
            yield {
                'name': lighting.css('div.lsooF span::text').get(),  # Проверьте и замените селектор для названия
                'price': lighting.css('div.pY3d2 span::text').get(),  # Проверьте и замените селектор для цены
                'url': response.urljoin(lighting.css('a').attrib['href'])  # Формируем полный URL
            }
