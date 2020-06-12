# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome('')
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_css_selector("input[class='btn_action']").click()
    print ('Access to the Web Page was successful.')
    driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
    driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
    driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
    driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
    driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
    driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
    print ('All 6 clothes are in the basket.')
    driver.find_element_by_css_selector("svg[class='svg-inline--fa fa-shopping-cart fa-w-18 fa-3x ']").click()
    driver.find_element_by_css_selector("button[class='btn_secondary cart_button']").click()
    driver.find_element_by_css_selector("button[class='btn_secondary cart_button']").click()
    driver.find_element_by_css_selector("button[class='btn_secondary cart_button']").click()
    driver.find_element_by_css_selector("button[class='btn_secondary cart_button']").click()
    driver.find_element_by_css_selector("button[class='btn_secondary cart_button']").click()
    driver.find_element_by_css_selector("button[class='btn_secondary cart_button']").click()
    print ('All 6 clothes where removed from the basket.')

login('standard_user', 'secret_sauce')

