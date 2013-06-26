from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from dilbert.items import DilbertStrip
from urlparse import urljoin

class DilbertSpider(BaseSpider):
    name = 'dilbert'
    start_urls = ['http://dilbert.com/']

    def __init__(self, name=None, **kwargs):
        super(DilbertSpider, self).__init__(name, **kwargs)
        self.link_extractor = SgmlLinkExtractor(allow='/strips/comic/20(10|11|12|13)-[0-9-]{5}/$')

    def parse(self, response):
        for link in self.link_extractor.extract_links(response):
            yield Request(link.url, self.parse)
        strip_path = HtmlXPathSelector(response).select('//div[@class="STR_Image"]/img/@src').extract()
        if strip_path:
            strip_path = urljoin(response.url, strip_path[0])
            strip = DilbertStrip()
            strip['image'] = strip_path
            strip['name'] = '%s.%s' % (response.url.split('/')[-2], strip_path.split('.')[-1])
            yield strip
