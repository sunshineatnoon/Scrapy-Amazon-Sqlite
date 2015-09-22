# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class AmazonItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #name of image
    Name = Field()
    #imagepath on local file system
    Path = Field()
    #commodity url
    Source = Field()
    #deep learning feature of image
    Feature = Field()
    
