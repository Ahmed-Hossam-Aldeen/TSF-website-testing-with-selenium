#Full script
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions

options = EdgeOptions()
options.use_chromium = True

# Using Chrome to access thesparksfoundationsingapore.org
driver = Edge(options=options)
# Open the website
driver.get("https://www.thesparksfoundationsingapore.org/")
driver.maximize_window()

#Making sure logo exists
logo = driver.find_element_by_xpath("//img[ @src='/images/logo_small.png']")
if logo:
    print("Logo found")
    logo.click()
else:
    print("Logo not found")

#Opening Guiding Principles
about = driver.find_element_by_xpath("//a[ @data-hover='About']")
about.click()
about.send_keys(Keys.TAB + Keys.TAB + Keys.RETURN)

#Checking if title is correct
title = driver.find_element_by_tag_name("h2")
if title.text == "Guiding Principles":
    print("title is correct")

#Accessing contact us
contact = driver.find_element_by_xpath("//a[@data-hover='Contact Us']")
contact.click()

#Checking if website has instagram link
instagram = driver.find_element_by_xpath("//a[@href='https://instagram.com/thesparksfoundation.info']")
if instagram:
    print("instagram account found!")
else:
    print("instagram account not found!")

#Access Corporate Programs
driver.find_element_by_link_text("Career Choices").click()
driver.find_element_by_link_text("Corporate Programs").click()

#Printing all elements with h4 tag
h4_tags = driver.find_elements_by_tag_name("h4")
for i in h4_tags:
    print(i.text)

#Accessing Student SOS Program
driver.find_element_by_link_text("LINKS App").click()
driver.execute_script("window.scrollTo(0, 120)") 
time.sleep(1)
driver.find_element_by_link_text("Student SOS Program").click()

#Printing the Sparks Foundation Vision
driver.execute_script("window.scrollTo(0, 800)") 
span_tags = driver.find_elements_by_tag_name("span")
print(span_tags[12].text+":\n"+span_tags[13].text)


