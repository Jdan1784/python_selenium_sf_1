# python -m pip install selenium

# from lib2to3.pgen2 import driver
from selenium import webdriver # Штука, которая позвалялет запускать браузер в режиме авто управления.
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome("C/Users/358/project/test_gid/SkillFactory/python_selenium_sf/chromedriver") # Чтобы запустить браузер нужна эта команда. При этом к Chrome нужно подключить определенную вещь.
driver.get("http://google.com")
driver.find_element(By.XPATH, "//input[@title=\"Поиск\"]").send_keys('SkillFactory' + Keys.RETURN)

driver.save_screenshot('sf.png')
sleep(3)
# driver.save_screenshot('pet_home987654e3.png')
# sleep(100)
driver.quit()
