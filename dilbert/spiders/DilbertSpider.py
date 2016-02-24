from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from dilbert.items import DilbertStrip
from urlparse import urljoin

class DilbertSpider(BaseSpider):
    name = 'dilbert'
    start_urls = ['http://dilbert.com/strip/2010-01-01']

    def __init__(self, name=None, **kwargs):
        super(DilbertSpider, self).__init__(name, **kwargs)
        self.link_extractor = SgmlLinkExtractor(allow='/strip/20(10|11|12|13)-[0-9-]{5}$')

    def parse(self, response):
        for link in self.link_extractor.extract_links(response):
            yield Request(link.url, self.parse)
        strip_path = HtmlXPathSelector(response).select('//meta[@property="og:image"]/@content').extract()
        if strip_path:
            strip = DilbertStrip()
            strip['image'] = strip_path.pop()
            strip['name'] = '%s.gif' % response.url.split('/')[-1]
            yield strip
