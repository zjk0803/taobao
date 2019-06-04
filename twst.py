from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'D:\google浏览器\Application\chromedriver.exe')
driver.get('https://www.baidu.com/')
print(driver.title)
