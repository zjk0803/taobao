# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
class TaobaoPipeline(object):
    def open_spider(self,spider):
        print("opened")
        try:
            self.con = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",passwd = "123456",db = "TB",charset='utf8')
            self.cursor = self.con.cursor(pymysql.cursors.DictCursor)
            self.cursor.execute("delete from tbdb")
            self.opened = True
            self.count = 0
        except Exception as err:
            print(err)
            self.opened = False
    def close_spider(self,spider):
        if self.opened:
            self.con.commit()
            self.con.close()
            self.opened = False
        print("close")
        print("总共爬取",self.count,"个视频")
    def process_item(self,item,spider):
        try:
            print((item["price"]))
            print((item["title"]))
            print((item["shop"]))
            print(item["image"])
            print((item["deal"]))
            print((item["location"]))
            print()
            if self.opened:
                self.cursor.execute("insert into tbdb(price,title,shop,image,deal,location)values (%s,%s,%s,%s,%s,%s)",(item["price"],item["title"],item["shop"],item["image"],item["deal"],item["location"]))
                self.count += 1

        except Exception as err:
            print(err)
        return item
