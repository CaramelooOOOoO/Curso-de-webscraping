from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule 
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

class Articulo(Item):
    titulo = Field()
    descripcion = Field()


class MercadoLibreCrawler(CrawlSpider):
    name = 'mercadolibre'

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
        'CLOSESPIDER_PAGECOUNT': 10 # Numero maximo de paginas en las cuales voy a descargar items. Scrapy se cierra cuando alcanza este numero
    }


    allowed_domains = ['articulo.mercadolibre.com.pe', 'listado.mercadolibre.com.pe']

    start_urls=['https://listado.mercadolibre.com.pe/celulares-smartphones']

    download_delay = 1

    rules=(

        Rule(
            LinkExtractor(
              allow=r'/_Desde_\d+'
            ),follow=True),
    
        Rule(
            LinkExtractor(
             allow=r'/MPE-'
            ),follow=True, callback='parse_items'),

    )
    
    
    

    def parse_items(self, response):

        item = ItemLoader(Articulo(), response)

        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('descripcion' , '//p[@class="ui-pdp-description__content"]/text()')

        yield item.load_item()
    
