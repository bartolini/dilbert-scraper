# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from urllib import urlretrieve
from os import path

class DilbertPipeline(object):

    def process_item(self, item, spider):
        file_name = path.join(spider.settings['DOWNLOAD_INTO_FOLDER'], item['name'])
        urlretrieve(item['image'], filename=file_name)
        raise DropItem
