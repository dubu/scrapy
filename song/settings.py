# Scrapy settings for song project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'song'

SPIDER_MODULES = ['song.spiders']
NEWSPIDER_MODULE = 'song.spiders'

ITEM_PIPELINES = { 'song.pipelines.SongPipeline':1 }