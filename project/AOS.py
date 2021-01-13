from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path= r"C:\Users\User\Desktop\New folder\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()
time.sleep(3)

driver.find_element_by_id("speakersTxt").click()
driver.find_element_by_id("22").click()
driver.find_element_by_css_selector('div[increment-value-attr="+"]').click()
driver.find_element_by_name("save_to_cart").click()

driver.find_element_by_css_selector("[href='#/shoppingCart']").click()
print(driver.find_elements_by_css_selector('tbody>tr>td[class="smollCell quantityMobile"]>label[class="ng-binding"]').get_attribute("value"))


#table = driver.find_elements_by_css_selector("[class='fixedTableEdgeCompatibility']")
# tbody = driver.find_elements_by_css_selector("[class='fixedTableEdgeCompatibility']>tbody")
# products = 0
# for i in range(len(tbody)):
#     amount = driver.find_elements_by_css_selector("td[class='smollCell quantityMobile']>label")
#     print(driver.find_elements_by_css_selector("#shoppingCart > table > tbody > tr > td:nth-child(5) > label.ng-binding"))
#     print(amount[0])
