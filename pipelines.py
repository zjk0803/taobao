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
            self.con = pymysql.connect(host = "127.0.0.1",port = 3306,user = "root",passwd = "123456",db = "Bilibili",charset='utf8')
            self.cursor = self.con.cursor(pymysql.cursors.DictCursor)
            self.cursor.execute("delete from test")
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
            print((item["title"]))
            print((item["num"]))
            print((item["top"]))
            print(item["author"])
            print((item["comment_num"]))
            print()
            if self.opened:
                self.cursor.execute("insert into test(title,num,top,author,comment_num)values (%s,%s,%s,%s,%s)",(item["title"],item["num"],item["top"],item["author"],item["comment_num"]))
                self.count += 1

        except Exception as err:
            print(err)
        return item
