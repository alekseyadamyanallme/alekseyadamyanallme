# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest11():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test11(self):
    # Test name: test11
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://resumesimple.dev.hsworld.ru/")
    # 2 | setWindowSize | 977x535 | 
    self.driver.set_window_size(977, 535)
    # 3 | click | css=.btn-br | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-br").click()
    # 4 | click | css=.form__input:nth-child(1) > input | 
    self.driver.find_element(By.CSS_SELECTOR, ".form__input:nth-child(1) > input").click()
    # 5 | click | css=.form__input:nth-child(1) > input | 
    self.driver.find_element(By.CSS_SELECTOR, ".form__input:nth-child(1) > input").click()
    # 6 | type | css=.form__input:nth-child(1) > input | loginfortesttask@yandex.ru
    self.driver.find_element(By.CSS_SELECTOR, ".form__input:nth-child(1) > input").send_keys("loginfortesttask@yandex.ru")
    # 7 | type | css=.form__input:nth-child(2) > input | 123456789Aa
    self.driver.find_element(By.CSS_SELECTOR, ".form__input:nth-child(2) > input").send_keys("123456789Aa")
    # 8 | click | css=.btn-bg--blue:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-bg--blue:nth-child(3)").click()
    # 9 | mouseOver | css=.btn-bg--blue:nth-child(3) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-bg--blue:nth-child(3)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 10 | click | linkText=?????????????????????? ???????????? | 
    self.driver.find_element(By.LINK_TEXT, "?????????????????????? ????????????").click()
    # 11 | click | id=input-125 | 
    self.driver.find_element(By.ID, "input-125").click()
    # 12 | type | id=input-125 | 12345
    self.driver.find_element(By.ID, "input-125").send_keys("12345")
    # 13 | click | id=input-139 | 
    self.driver.find_element(By.ID, "input-139").click()
    # 14 | type | id=input-139 | qwerty
    self.driver.find_element(By.ID, "input-139").send_keys("qwerty")
    # 15 | click | id=input-142 | 
    self.driver.find_element(By.ID, "input-142").click()
    # 16 | type | id=input-142 | asdfg
    self.driver.find_element(By.ID, "input-142").send_keys("asdfg")
    # 17 | click | id=input-145 | 
    self.driver.find_element(By.ID, "input-145").click()
    # 18 | type | id=input-145 | zxcvb
    self.driver.find_element(By.ID, "input-145").send_keys("zxcvb")
    # 19 | click | id=input-173 | 
    self.driver.find_element(By.ID, "input-173").click()
    # 20 | mouseOver | css=.dark-blue | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".dark-blue")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 21 | type | id=input-173 | zxcvbnm
    self.driver.find_element(By.ID, "input-173").send_keys("zxcvbnm")
    # 22 | click | css=.dark-blue | 
    self.driver.find_element(By.CSS_SELECTOR, ".dark-blue").click()
    # 23 | mouseOut | css=.dark-blue:nth-child(2) | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 24 | click | css=.dark-blue:nth-child(2) > .v-btn__content | 
    self.driver.find_element(By.CSS_SELECTOR, ".dark-blue:nth-child(2) > .v-btn__content").click()
    # 25 | click | css=.dark-blue:nth-child(2) > .v-btn__content | 
    self.driver.find_element(By.CSS_SELECTOR, ".dark-blue:nth-child(2) > .v-btn__content").click()
    # 26 | mouseOver | css=.dark-blue:nth-child(2) > .v-btn__content | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".dark-blue:nth-child(2) > .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 27 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 28 | click | linkText=?????? ???????????? | 
    self.driver.find_element(By.LINK_TEXT, "?????? ????????????").click()
    # 29 | click | css=.mdi-delete | 
    self.driver.find_element(By.CSS_SELECTOR, ".mdi-delete").click()
    # 30 | click | css=.justify-space-between > .v-btn:nth-child(1) > .v-btn__content | 
    self.driver.find_element(By.CSS_SELECTOR, ".justify-space-between > .v-btn:nth-child(1) > .v-btn__content").click()
    # 31 | click | css=.v-btn--is-elevated:nth-child(3) > .v-btn__content | 
    self.driver.find_element(By.CSS_SELECTOR, ".v-btn--is-elevated:nth-child(3) > .v-btn__content").click()
    # 32 | mouseDownAt | linkText=?????????? | 18.13751220703125,14.799997329711914
    element = self.driver.find_element(By.LINK_TEXT, "??????????")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 33 | mouseMoveAt | linkText=?????????? | 18.13751220703125,14.799997329711914
    element = self.driver.find_element(By.LINK_TEXT, "??????????")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 34 | mouseUpAt | linkText=?????????? | 18.13751220703125,14.799997329711914
    element = self.driver.find_element(By.LINK_TEXT, "??????????")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 35 | click | linkText=?????????? | 
    self.driver.find_element(By.LINK_TEXT, "??????????").click()
  
