import scrapy
import urllib
from amazon.items import AmazonItem


class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amazon"
    allowed_domains = ["amazon.com"]
    '''
    start_urls = ["http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=backpack",
                  "http://www.amazon.com/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Abackpack&page=2&keywords=backpack&ie=UTF8&qid=1442907452&spIA=B00YCRMZXW,B010HWLMMA"
                  ]
    '''
    def start_requests(self):
        yield scrapy.Request("http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=backpack",self.parse)
        for i in range(2,20):
            yield scrapy.Request("http://www.amazon.com/s/ref=sr_pg_2?rh=i%3Aaps%2Ck%3Abackpack&page="+str(i)+"&keywords=backpack&ie=UTF8&qid=1442907452&spIA=B00YCRMZXW,B010HWLMMA",self.parse)
    
    
    
    def parse(self,response):
        namelist = response.xpath('//a[@class="a-link-normal s-access-detail-page  a-text-normal"]/@title').extract()
        htmllist = response.xpath('//a[@class="a-link-normal s-access-detail-page  a-text-normal"]/@href').extract()
        imglist = response.xpath('//a[@class="a-link-normal a-text-normal"]/img/@src').extract()
        listlength = len(namelist)
        
        for i in range(0,listlength):
            item = AmazonItem()
            item['Name'] = namelist[i]
            item['Source'] = htmllist[i]
        
            urllib.urlretrieve(imglist[i],"/home/xuetingli/Desktop/crawlImages/"+str(amazonSpider.imgcount)+".jpg")
            item['Path'] = "/home/xuetingli/Desktop/crawlImages/"+str(amazonSpider.imgcount)+".jpg"
            amazonSpider.imgcount = amazonSpider.imgcount + 1
            yield item