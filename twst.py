import cv2
import numpy as np
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib
'''
img = cv2.imread("66.jpg",cv2.IMREAD_COLOR)
emptyImage = np.zeros(img.shape, np.uint8)

emptyImage2 = img.copy()



cv2.imshow("EmptyImage3", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9oVrfPR&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'



page = urllib.request.urlopen(url)
html = page.read()

soup = BeautifulSoup(html,'lxml')

for img in soup.select('img'):
    print(html)
    #print(img.attrs['src']