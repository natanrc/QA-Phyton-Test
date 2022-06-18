from selenium import webdriver
from _pytest import mark
from _pytest.mark.structures import Mark
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
#options.headless = True
#options.add_argument("--windows-size=1920,1080")

Login = [ 
    ("natantondok@gmail.com","r3birth07"),  #negative test case
    ("natan@gmail.com","R3birth07"),
    ("natan@gmail.com","R3birth")
]

@pytest.fixture
def setup():
    driver = webdriver.Chrome(options=options)
    #driver.maximize_window()
    driver.get("https://selfdeveloper.my.id/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()   
    

@pytest.mark.parametrize('a,b', Login)
def test_fail_log(setup,a,b):
    setup.find_element_by_name("email").send_keys(a)
    setup.find_element_by_name("password").send_keys(b)

    setup.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div[2]/button").click()
    setup.implicitly_wait(10)

    invalidText = setup.find_element_by_class_name("sr-only").text

    assert invalidText == "Close"

def test_success_log(setup): #positive test
    setup.find_element_by_name("email").send_keys("natantondok@gmail.com")
    setup.find_element_by_name("password").send_keys("R3birth07")
    setup.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div[1]/div/label/div/ins").click()
    setup.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div[2]/button").click()
    
    
    mainHeader = setup.find_element_by_class_name("logo-lg").text
    assert mainHeader == "Service Booking"

def test_link_forgot(setup):
    elm = setup.find_element_by_partial_link_text("Forgot")
    setup.implicitly_wait(10)
    elm.click()   
    time.sleep(2)
