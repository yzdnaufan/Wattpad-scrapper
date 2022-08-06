
from selenium import webdriver
import time

link = 'https://www.wattpad.com/login'

def get_html(category) :
    driver = webdriver.Chrome()
    driver.get(link)

    driver.find_element_by_class_name("btn-block.btn-primary").click()
    username = driver.find_element_by_id("login-username")
    password = driver.find_element_by_id("login-password")
    username.send_keys("dscnl001")
    password.send_keys("1234qwer")
    driver.find_element_by_class_name("btn.btn-lg.btn-primary.btn-block.enable.submit-btn").click()

    for cat in category:
        url_ = "https://www.wattpad.com/stories/"+str(cat)
        driver.get(url_)

        ScrollNumber = 5
        for i in range(1,ScrollNumber):
            driver.execute_script("window.scrollTo(1,50000)")
            time.sleep(5)
        
        
        fname = 'html/'+str(cat) + ".html"    
        with open(fname, "w", encoding="utf-8") as f:
            f.write(driver.page_source)

    driver.close()