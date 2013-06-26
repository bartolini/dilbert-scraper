# Scrapy settings for blank project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'dilbert'

SPIDER_MODULES = ['dilbert.spiders']
NEWSPIDER_MODULE = 'dilbert.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'blank (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'dilbert.pipelines.DilbertPipeline',
}

DOWNLOAD_INTO_FOLDER = './dilbert-strips/'

LOG_LEVEL = 'ERROR'