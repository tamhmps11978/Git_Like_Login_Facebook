import time

from selenium import webdriver
from selenium.webdriver import ActionChains
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

#
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
likes = driver.find_elements_by_xpath("//div[@class='tvfksri0 ozuftl9m']//div[@aria-label='Thích']")
actions = ActionChains(driver)
print(len(likes))
for i in range(0, 6):
    actions.move_to_element(likes[i]).perform()
    driver.execute_script("arguments[0].click();", likes[i])




