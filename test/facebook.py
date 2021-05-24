import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Tắt thông báo
options = Options()
options.add_argument("--disable-notifications")

# Khai báo biến driver
# driver = webdriver.chrome(executable_path="D:/Python/",chrome_options=options)
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
# Chạy website
driver.get("http://www.facebook.com/")

#Tìm thẻ input sau đó nhập email
input_email = driver.find_element_by_id("email")
input_email.send_keys('tamgoescf2@gmail.com')
time.sleep(2)

#Tìm thẻ input passwrod
input_pass = driver.find_element_by_id('pass')
input_pass.send_keys('Hminhtam')
time.sleep(2)

#ấn nút đăng nhập
btn_submit = driver.find_element_by_name('login')
btn_submit.click()









