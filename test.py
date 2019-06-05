import re
import requests

#定义一个类

class T(object):
    def __init__(self):
        self.s = requests.Session()

    def status_code(self):
        url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
        headers_ = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.19 Safari/537.36'
        }
        res = self.s.get(url, headers=headers_).text
        u = re.findall(r'getQRCodeURL: "(.*?)"', res, re.S)[0]
        return u
    def rq_login(self):
        us = self.status_code()
        url = '{}'.format(us)
        headers = {
            'referer': 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.19 Safari/537.36'
        }
        res = self.s.get(url, headers=headers).json()
        print(res)
        rq_img = 'http:' + res.get('url')
        lgToken = res.get('lgToken')
        img_res = self.s.get(rq_img, headers=headers).content
        with open('img.png', 'wb')as f:
            f.write(img_res)


if __name__ == "__main__":
    chromedriver_path = "/D:\google浏览器\Application/chromedriver.exe"  # 改成你的chromedriver的完整路径地址
    weibo_username = "改成你的微博账号"  # 改成你的微博账号
    weibo_password = "改成你的微博密码"  # 改成你的微博密码

    a = T()

    a.rq_login()