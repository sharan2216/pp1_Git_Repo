import random
import time
from selenium import webdriver
# from time import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
#initialize webdriver
driver=webdriver.Chrome(options=options)

#if required update the chromeDriver version at "C:\Windows" location
#open URL and maximize window
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
#phone button
phone=driver.find_element(By.XPATH,"//a[text()='Phones & PDAs']")
phone.click()
time.sleep(2)
#iphone
iphone=driver.find_element(By.XPATH,"//a[text()='iPhone']")
iphone.click()
time.sleep(2)
#first picture
first_pic= driver.find_element(By.XPATH,"//ul[@class='thumbnails']/li[1]")
first_pic.click()
time.sleep(1)

#next picture
next_click= driver.find_element(By.XPATH,"//button[@title='Next (Right arrow key)']")
next_click.click()

for i in range(0,5):
    next_click.click()
    time.sleep(1)

#save screenshot
# driver.get_screenshot_as_file('screenshot' + str(random.randint) + '.png')
driver.get_screenshot_as_file('./ScreenShots/ss.png')

x_button=driver.find_element(By.XPATH,"//button[@title='Close (Esc)']")
x_button.click()
time.sleep(2)

input_quantity=driver.find_element(By.XPATH,"//input[@id='input-quantity']")
input_quantity.click()
time.sleep(2)
input_quantity.clear()
time.sleep(1)
input_quantity.send_keys('2')
time.sleep(1)
button_cart=driver.find_element(By.XPATH,"//button[@id='button-cart']")
button_cart.click()
time.sleep(1)

cart_value_field = driver.find_element(By.XPATH,"//span[@id='cart-total']")
cartvalue_text=cart_value_field.text
actual_value= '2 item(s) - $246.40'
if actual_value in cartvalue_text:
    print("items added successfully in the cart")
time.sleep(3)
driver.get_screenshot_as_file('./ScreenShots/ss2.png')
time.sleep(2)

laptops=driver.find_element(By.XPATH,"//a[normalize-space()='Laptops & Notebooks']")

action = ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(1)
laptop_2=driver.find_element(By.XPATH,"//a[normalize-space()='Show AllLaptops & Notebooks']")
laptop_2.click()
time.sleep(2)

#click on HP laptop
HP=driver.find_element(By.XPATH,"//a[text()='HP LP3065']")
HP.click()

#scroll
add_to_button_2 = driver.find_element(By.XPATH,"//button[@id='button-cart']")
add_to_button_2.location_once_scrolled_into_view
time.sleep(2)

#calendar
calendar= driver.find_element(By.XPATH,"//i[@class='fa fa-calendar']")
calendar.click()
time.sleep(2)

next_click_calendar=driver.find_element(By.XPATH,"//th[@class='next'][1]")
month_year=driver.find_element(By.XPATH,"//th[@class='picker-switch']")
time.sleep(2)

# Dec 2023
while month_year.text!= 'December 2023':
    next_click_calendar.click()
time.sleep(2)

# day 31
calendar_date= driver.find_element(By.XPATH,"//td[text()='31']")
calendar_date.click()
time.sleep(2)

#add to button
add_to_button_2.click()
time.sleep(2)

driver.get_screenshot_as_file('./ScreenShots/ss3.png')
time.sleep(2)

#checkout
go_to_cart = driver.find_element(By.XPATH,"//span[@id='cart-total']")
go_to_cart.click()
time.sleep(2)

checkout=driver.find_element(By.XPATH,"//p[@class='text-right']//a[2]")
checkout.click()
product_name_ele= driver.find_element(By.XPATH,"//td[@class='text-left']//span[@class='text-danger']")
# alt=driver.switch_to.alert
# alert_message='Products marked with *** are not available in the desired quantity or not in stock!'

iphone_remove=driver.find_element(By.XPATH,"//tbody/tr[1]/td[4]/div[1]/span[1]/button[2]")
iphone_remove.click()
driver.get_screenshot_as_file("./ScreenShots/ss4.png")
# if '***' in product_name_ele:
#     driver.find_element(By.XPATH,"//tbody/tr[1]/td[4]/div[1]/span[1]/button[2]").click()
time.sleep(2)

# cart_link=driver.find_element(By.XPATH,"//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
# cart_link.click()
# go_to_cart.click()
time.sleep(2)

checkout2=driver.find_element(By.XPATH,"//a[@class='btn btn-primary']")
checkout2.click()
time.sleep(2)

guest_button = driver.find_element(By.XPATH,"//input[@value='guest']")
guest_button.click()
time.sleep(2)
driver.get_screenshot_as_file("./ScreenShots/ss5.png")

continue_1=driver.find_element(By.XPATH,"//input[@id='button-account']")
continue_1.click()
time.sleep(2)
driver.get_screenshot_as_file("./ScreenShots/ss6.png")

first_name=driver.find_element(By.XPATH,"//input[@id='input-payment-firstname']")
first_name.send_keys("sasa")
time.sleep(1)

last_name= driver.find_element(By.XPATH,"//input[@id='input-payment-lastname']")
last_name.send_keys("nasa")
time.sleep(1)

email=driver.find_element(By.XPATH,"//input[@id='input-payment-email']")
email.send_keys("sasa@gmail.com")
time.sleep(1)

telephone=driver.find_element(By.XPATH,"//input[@id='input-payment-telephone']")
telephone.send_keys("9876543210")
time.sleep(1)


address1=driver.find_element(By.XPATH,"//input[@id='input-payment-address-1']")
address1.send_keys("btm")
time.sleep(1)

city=driver.find_element(By.XPATH,"//input[@id='input-payment-city']")
city.send_keys("Bangalore")
time.sleep(1)

postal_code=driver.find_element(By.XPATH,"//input[@id='input-payment-postcode']")
postal_code.send_keys("560076")
time.sleep(2)

country_DD=driver.find_element(By.XPATH,"//select[@id='input-payment-country']")
country_DD.click()
dd_list=Select(country_DD)
dd_list.select_by_value("99")
time.sleep(2)

region_DD=driver.find_element(By.XPATH,"//select[@id='input-payment-zone']")
region_DD.click()
region_dd_list=Select(region_DD)
region_dd_list.select_by_value("1489")
driver.get_screenshot_as_file("./ScreenShots/ss7.png")
time.sleep(1)
continue_button1=driver.find_element(By.XPATH,"//input[@id='button-guest']")
continue_button1.click()
time.sleep(2)

continue_button2=driver.find_element(By.XPATH,"//input[@id='button-shipping-method']")
continue_button2.click()
driver.get_screenshot_as_file("./ScreenShots/ss8.png")
time.sleep(2)

terms_and_condition_button =driver.find_element(By.XPATH,"//input[@name='agree']")
terms_and_condition_button.click()
continue_button_3=driver.find_element(By.XPATH,"//input[@id='button-payment-method']")
continue_button_3.click()
driver.get_screenshot_as_file("./ScreenShots/ss9.png")
time.sleep(2)


# continue_button_4=driver.find_element(By.XPATH,"//input[@id='button-payment-method']")
# continue_button_4.click()
# driver.get_screenshot_as_file("./ScreenShots/ss10.png")
# time.sleep(1)

final_total_price=driver.find_element(By.XPATH,"//table[@class='table table-bordered table-hover']/tfoot/tr[3]").text
print("Final Price is : ",final_total_price)

continue_button_5=driver.find_element(By.XPATH,"//input[@id='button-confirm']")
continue_button_5.click()
driver.get_screenshot_as_file("./ScreenShots/ss11.png")
time.sleep(1)

expected_text="Your order has been placed!"
actual_text=driver.find_element(By.XPATH,"//h1[normalize-space()='Your order has been placed!']").text
if actual_text.__eq__(expected_text):
    print("Order got Placed....!!!!")

continue_button_6=driver.find_element(By.XPATH,"//a[normalize-space()='Continue']")
continue_button_6.click()
driver.get_screenshot_as_file("./ScreenShots/ss12.png")


time.sleep(2)
driver.close()


