import logging
import time
import string
import conftest
from Support import autoconfig
from selenium.webdriver.common.keys import Keys
import random

def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def open(page):
    conftest.wd.get(page)


def find_element(loc):
    element = conftest.wd.find_element_by_xpath(loc)
    return element


def find_elements(loc):
    elements = conftest.wd.find_elements_by_xpath(loc)
    return elements


def is_element_visible(locator):
    logging.debug("Verify that element '" + locator + "' is visible")
    try:
        if find_element(locator).is_displayed():
            return True
        else:
            return False
    except:
        return False


def is_element_present(locator):
    logging.debug("Verify that element '" + locator + "' is visible")
    try:
        if find_element(locator):
            return True
        else:
            return False
    except:
        return False


def wait_for_element_present(locator):
    logging.debug("Wait for element '" + locator + "' to be visible")
    for i in range(autoconfig.timeout):
        try:
            if is_element_present(locator): return
        except:
            pass
        time.sleep(0.25)
    else:
        return


def wait_for_element_visible(locator):
    logging.debug("Wait for element '" + locator + "' to be visible")
    for i in range(autoconfig.timeout):
        try:
            if is_element_visible(locator): return
        except:
            pass
        time.sleep(0.25)
    else:
        return


def select_window(i):
    print conftest.wd.window_handles
    conftest.wd.switch_to.window(conftest.wd.window_handles[i])


def wait_for_element_not_visible(locator):
    logging.debug("Wait for element '" + locator + "' to be NOT visible")
    for i in range(autoconfig.timeout):
        try:
            if not is_element_visible(locator): return
        except:
            pass
        time.sleep(0.25)
    else:
        return


def get_alert():
    try:
        alert = conftest.wd.switch_to_alert()
        alert.accept()
    except:
        pass


def wait_for_alert():
    for i in range(autoconfig.timeout):
        try:
            alert = conftest.wd.switch_to_alert()
            assert alert.dismiss()
        except:
            pass
        time.sleep(0.25)
    else:
        return


def send_keys_for_open_emodji(loc):
    el = find_element(loc)
    el.send_keys(Keys.CONTROL, Keys.SHIFT, "2")


def send_keys_for_send_mail(loc):
    el = find_element(loc)
    el.send_keys(Keys.CONTROL, Keys.ENTER)


def click(loc):
    find_element(loc).click()


def mouse_over(loc):
    el = find_element(loc)
    el.mouse_over()


def type(loc, text):
    if text is not None:
        el = find_element(loc)
        el.click()
        el.clear()
        el.send_keys(text)