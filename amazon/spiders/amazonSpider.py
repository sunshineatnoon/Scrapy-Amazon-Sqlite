import scrapy
import urllib
from amazon.items import AmazonItem

class amazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = ["http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=backpack"]
    
    def parse(self,response):
        namelist = response.xpath('//a[@class="a-link-normal s-access-detail-page  a-text-normal"]/@title').extract()
        htmllist = response.xpath('//a[@class="a-link-normal s-access-detail-page  a-text-normal"]/@href').extract()
        imglist = response.xpath('//a[@class="a-link-normal a-text-normal"]/img/@src').extract()
        listlength = len(namelist)
        
        for i in range(0,listlength):
            item = AmazonItem()
            item['Name'] = namelist[i]
            item['Source'] = htmllist[i]
        
            urllib.urlretrieve(imglist[i],"/home/xuetingli/Desktop/crawlImages/"+str(i)+".jpg")
            item['Path'] = "/home/xuetingli/Desktop/crawlImages/"+str(i)+".jpg"
            yield item