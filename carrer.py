import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
# from helper import *
import time

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.61 Safari/537.36'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument(f'user-agent={user_agent}')


# Functions created by me for reusability
def save(final_data):
    
    json_object = json.dumps(final_data, indent=4, ensure_ascii=False)
    with open("data.json", "w", encoding='utf8') as outfile:
        outfile.write(json_object)


def check_exists_by_xpath_href(driver, xpath: str):
    try:
        value = driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        print(f'XPATH NOT FOUND ---- || {xpath}')
        return "null"
    return value.get_attribute('href')


def check_exists_by_xpath_text(driver, xpath):
    try:
        value = driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        print(f'XPATH NOT FOUND ---- || {xpath}')
        return "null"
    return value.text


def check_exists_by_xpath_src(driver, xpath):
    try:
        value = driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        print(f'XPATH NOT FOUND ---- || {xpath}')
        return "null"
    return value.get_attribute('src')


def check_exists_by_xpath_href(driver, xpath: str):
    try:
        value = driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        print(f'XPATH NOT FOUND ---- || {xpath}')
        return "null"
    return value.get_attribute('href')


def check_exists_by_classname(driver, xpath):
    try:
        value = driver.find_element(By.CLASS_NAME, xpath)
    except NoSuchElementException:
        return "null"
    return value


# MAIN CODE
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)

start_url = 'https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=bjmtuc.club'
# start_url = 'https://in.godaddy.com/'

driver.get(start_url)   


price1= check_exists_by_xpath_text(driver, '/html/body/main/div/div/div/div/div[3]/div[1]/div[1]/div[2]/div/div[3]/div/div[1]/div[1]/div/span[1]/span')
print(price1)


price2= check_exists_by_xpath_text(driver, '/html/body/main/div/div/div/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div/div[1]/div[1]/div/span[1]/span')
print(price2)