from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome(executable_path=r'D:\google浏览器\Application\chromedriver.exe')
wait = WebDriverWait(browser,10)

KEYWORD = 'ipad'

def index_page(page):
    """
    抓取索引页
    :param page:
    :return:
    """
    print('正在爬取第',page,'页')
    try:
        url = 'https://list.tmall.com/search_product.htm?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-pager div.form>input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form> span.btn.J_Submit'))
            )

            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active >span'),str(page))
        )
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page()


