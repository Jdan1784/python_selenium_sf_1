# python -m pip install selenium

# from lib2to3.pgen2 import driver
from selenium import webdriver # Штука, которая позвалялет запускать браузер в режиме авто управления.
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome("C/Users/358/project/test_gid/SkillFactory/python_selenium_sf/chromedriver")
driver.get("https://130.193.37.179/app/pets")
t = (driver.find_elements(By.XPATH, "//*[@id=\"image\"]/img"))[0].clic()
print(t)

sleep(3)
# driver.save_screenshot('pet_home987654e3.png')
# sleep(100)
driver.quit()
