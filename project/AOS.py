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

###############################################################################
"""FIRST TASK"""
###############################################################################
def values_from_a_table(table_css_selector, place):
    """this function gets a table's css_selectors, place of the value you want.
       the function return the value in a list.
    """
    table = driver.find_element_by_css_selector(f"{table_css_selector}")
    rows = table.find_elements_by_tag_name("tr")
    answer = []
    for row in rows:
        cells = row.find_elements_by_tag_name("td")
        for i in range(len(cells)):
            if i == place and i != len(cells) - 1:
                answer.append(cells[i].text)
    return answer

"""
y = values_from_a_table( "[class='fixedTableEdgeCompatibility']", 4)
total_amount = 0
for i in y:
    total_amount += int(i)
if total_amount == int(driver.find_element_by_css_selector('[id="shoppingCartLink"]>span').text):
    print("True")
"""
############ fix it!
# WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located(By.CSS_SELECTOR("[ng-show='cart.productsInCart.length > 0']>tfoot>tr>td>span>label")))
# time.sleep(2)
# word = str(driver.find_element_by_css_selector("[ng-show='cart.productsInCart.length > 0']>tfoot>tr>td>span>label").text)
# x = word.split()[0].replace("(","")
# print(x)
# if x == y:
#     print("True")

################################################################
"""DONE!"""
################################################################
"""task 2"""
################################################################
# table1 = driver.find_element_by_css_selector("#toolTipCart > div > table")
# rows = table1.find_elements_by_tag_name("tr")
# pop_up_products_name = []
# for row in rows:
#     cells = row.find_elements_by_tag_name("td")
#     for i in range(len(cells)):
#         if i == 1 and i != len(cells) - 1:
#            pop_up_products_name.append(cells[i].find_element_by_tag_name("h3").text)
# print(pop_up_products_name)
# cart_page_products_name = values_from_a_table("[class='fixedTableEdgeCompatibility']", 1)
# print(cart_page_products_name)
# if pop_up_products_name == cart_page_products_name:
#     print("True")
# else:
#     print("False")
#

#gets values from the table at the cart page
"""
table = driver.find_element_by_css_selector("[class='fixedTableEdgeCompatibility']")
rows = table.find_elements_by_tag_name("tr")
products_names = []
products_color = []
products_quantity =[]
products_price = []
for row in rows:
    cells = row.find_elements_by_tag_name("td")
    for i in range(len(cells)):
        if i == 1 and i != len(cells) - 1:
            products_names.append(cells[i].text)
        if i == 3 and i != len(cells) - 1:
            products_color.append(cells[i].find_element_by_tag_name("span").get_attribute("title"))
        if i == 4 and i != len(cells) -1:
            products_quantity.append(cells[i].text)
            # help with getting the price
        if i ==5 and i != len(cells) -1:
            products_price.append(cells[i].find_element_by_tag_name("p").text)
print(products_names)
print(products_color)
print(products_quantity)
# print(products_price)
"""

#FAIL TRY TO GET THE VELUES IN THE POP_UP TABLE
table = driver.find_element_by_css_selector("[ng-show='cart.productsInCart.length > 0']")
rows = table.find_elements_by_tag_name("tr")
pop_up_products_names = []
pop_up_products_color = []
pop_up_products_quantity =[]
pop_up_products_price = []

for row in rows:
    cells = row.find_elements_by_tag_name("td")
    for i in range(len(cells)):
        if i == 1 and i != len(cells) - 1:
            pop_up_products_names.append(cells[i].find_element_by_tag_name("h3").text)
        if i == 3 and i != len(cells) - 1:
            pop_up_products_color.append(cells[i].find_elements_by_class_name("ng-binding")[2].find_element_by_tag_name("span").text)
        if i == 4 and i != len(cells) -1:
            pop_up_products_quantity.append(cells[i].find_elements_by_class_name("ng-binding")[1].text)
            # help with getting the price
        if i ==5 and i != len(cells) -1:
            pop_up_products_price.append(cells[i].find_elements_by_class_name("price roboto-regular ng-binding").text)
print(pop_up_products_names)
print(pop_up_products_color)
print(pop_up_products_quantity)
print(pop_up_products_price)