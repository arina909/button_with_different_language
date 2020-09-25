import time
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_bottom_add_to_basket(browser):
    browser.get(link)
    time.sleep(5)
    button=browser.find_element_by_class_name("btn.btn-add-to-basket")
    assert button, "there is no button"
