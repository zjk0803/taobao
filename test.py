import re
import requests
import cv2
import numpy as np
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


    a = T()

    a.rq_login()
img = cv2.imread("img.png",cv2.IMREAD_COLOR)
emptyImage = np.zeros(img.shape, np.uint8)

emptyImage2 = img.copy()



cv2.imshow("EmptyImage3", img)
cv2.waitKey(0)
cv2.destroyAllWindows()