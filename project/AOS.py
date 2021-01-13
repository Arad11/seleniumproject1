from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path= r"D:\python\chromedriver.exe")
#driver = webdriver.Chrome(executable_path= r"C:\Users\User\Desktop\New folder\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()
time.sleep(3)

#here we are buying 3 different products
driver.find_element_by_id("speakersTxt").click()
driver.find_element_by_id("22").click()
driver.find_element_by_css_selector('div[increment-value-attr="+"]').click()
driver.find_element_by_name("save_to_cart").click()
driver.find_element_by_css_selector("body > div.uiview.ng-scope > nav > a:nth-child(2)").click()
driver.find_element_by_id("20").click()
driver.find_element_by_css_selector('div[increment-value-attr="+"]').click()
driver.find_element_by_name("save_to_cart").click()
driver.find_element_by_css_selector("body > div.uiview.ng-scope > nav > a:nth-child(2)").click()
driver.find_element_by_id("21").click()
driver.find_element_by_css_selector('div[increment-value-attr="+"]').click()
driver.find_element_by_name("save_to_cart").click()

#here we are going to the cart page
driver.find_element_by_css_selector("[href='#/shoppingCart']").click()
# here we calculate how much products are in the cart
"""
table = driver.find_element_by_css_selector("[class='fixedTableEdgeCompatibility']")
rows = table.find_elements_by_tag_name("tr")
products_amount = 0
for row in rows:
    cells = row.find_elements_by_tag_name("td")
    for cell in cells:
        try:
            x = int(cell.text)
            products_amount += x
        except: ValueError

    print()
print(products_amount)
"""
def how_much_products(table_css_selector):
    """
    this action gets a css_selector of a table, and counts the numbers inside
    """
    print(table_css_selector)
    table = driver.find_element_by_css_selector(f"{table_css_selector}")
    rows = table.find_elements_by_tag_name("tr")
    products_amount = 0
    for row in rows:
        cells = row.find_elements_by_tag_name("td")
        for cell in cells:
            try:
                x = int(cell.text)
                products_amount += x
            except: ValueError
    return products_amount
y = how_much_products( "[class='fixedTableEdgeCompatibility']")


if y ==int(driver.find_element_by_css_selector('[id="shoppingCartLink"]>span').text):
    print("True")