from BrainBucket.BDDBehave.Chapter_15_2.config_reader import ConfigReader
from BrainBucket.webelements.browser import Browser
from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
import time


def before_feature(context, feature):
    configs = ConfigReader("BrainBucket/BDDBehave/Chapter_15_2/15_2_2/config.ini")
    context.configs = configs
    browser = Browser(configs.get_url(), configs.get_browser(), configs.get_wait_time())
    context.browser = browser


def before_scenario(context, scenario):
    print('I have no idea what action put in this option')


def after_scenario(context, scenario):# click continue btn
    browser = context.browser
    continue_btn = Element(browser, By.XPATH, "//*[@class='btn btn-primary']")
    continue_btn.click()
    time.sleep(3)



def after_feature(context, scenario):# checking that we are inside new account
    browser = context.browser
    my_account_tag = Element(browser, By.XPATH, '//*[@id="content"]/h2[1]')
    assert my_account_tag.get_text() == 'My Account'
    time.sleep(3)
