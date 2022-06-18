from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://selfdeveloper.my.id")
    driver.find_element_by_name("email").send_keys("natantondok@gmail.com")
    driver.find_element_by_name("password").send_keys("R3birth07")
    driver.find_element_by_class_name("col-xs-4").click()

    driver.find_element_by_xpath("/html/body/div[2]/aside/section/ul/li[4]/a").click()
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/section[1]/ol/li/a").click()
    yield driver
    driver.quit() 

def test_upload(setup):
    setup.find_element_by_class_name("form-group")
    setup.find_element_by_name("title").send_keys("promotion")

    chose = setup.find_element_by_id("type")
    element = Select(chose)
    element.select_by_index(0)
    time.sleep(3)

    setup.find_element_by_class_name("row")
    setup.find_element_by_name("image").send_keys("D://sport-car-icon-0.png")
    time.sleep(3)

    setup.find_element_by_class_name("box-body")
    setup.find_element_by_name("addcatg").click()