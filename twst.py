# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import time
import random
from pyquery import PyQuery as pq



class loginTB(object):
    def __init__(self):
        self.driver = webdriver.Chrome("D:\google浏览器\Application\chromedriver1.exe")
        self.driver.maximize_window()
        # 设置一个智能等待
        self.wait = WebDriverWait(self.driver,5)




    #登录模块
    def login(self):
        url = 'https://login.taobao.com/member/login.html'
        self.driver.get(url)
        try:
            # 寻找密码登陆按钮
            login_links = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='扫码登录']"))
            )
            login_links.click()
        except TimeoutException as e:
            print("找不到登陆入口，原因是：", e)

            try:
                # 试探能否找到个人信息，如果找不到说明登录失败
                user_info = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='m-userinfo']"))
                )
                print('已经登陆成功，进入了个人中心')
            except TimeoutException:
                try:
                    self.driver.find_element_by_xpath("//div[@class='avatar-wrapper']")
                    print('已经登录成功，进入了淘宝网首页')
                except Exception as e:
                    print("登录失败")

    #爬取淘宝
    def tb_spider(self):
        for page in range(1,1000):

            # 等待该页面全部已买到的宝贝商品数据加载完毕
            good_total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tp-bought-root > div.js-order-container')))

            # 获取本页面源代码
            html = self.browser.page_source

            # pq模块解析网页源代码
            doc = pq(html)

            # # 存储该页已经买到的宝贝数据
            good_items = doc('#tp-bought-root .js-order-container').items()

            # 遍历该页的所有宝贝
            for item in good_items:
                good_time_and_id = item.find('.bought-wrapper-mod__head-info-cell___29cDO').text().replace('\n',"").replace('\r',"")
                good_merchant = item.find('.seller-mod__container___1w0Cx').text().replace('\n',"").replace('\r',"")
                good_name = item.find('.sol-mod__no-br___1PwLO').text().replace('\n', "").replace('\r', "")
                # 只列出商品购买时间、订单号、商家名称、商品名称
                # 其余的请自己实践获取
                print(good_time_and_id, good_merchant, good_name)

            print('\n\n')

            # 大部分人被检测为机器人就是因为进一步模拟人工操作
            # 模拟人工向下浏览商品，即进行模拟下滑操作，防止被识别出是机器人
            # 随机滑动延时时间
            swipe_time = random.randint(1, 3)
            self.swipe_down(swipe_time)


            # 等待下一页按钮 出现
            good_total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.pagination-next')))
            # 点击下一页按钮
            good_total.click()
            sleep(2)




if __name__ == '__main__':
    t = time.time()
    l = loginTB()
    l.login()
    l.tb_spider()
    print('登录完成，耗时{:.2f}秒'.format(float(time.time()-t)))