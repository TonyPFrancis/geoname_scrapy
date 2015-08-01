# -*- coding: utf-8 -*-
import os

# Scrapy settings for geoname project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'geoname'

SPIDER_MODULES = ['geoname.spiders']
NEWSPIDER_MODULE = 'geoname.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'geoname (+http://www.yourdomain.com)'

AUTOTHROTTLE_ENABLED = True


# ********************************

OUTPUT_FOLDER_NAME = 'OUTPUT'
OUTPUT_FOLDER_PATH = os.path.join(os.getcwd(), OUTPUT_FOLDER_NAME)

