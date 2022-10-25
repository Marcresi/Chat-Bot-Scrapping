import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
# from helper import *
import time

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument(f'user-agent={user_agent}')



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
final_data = []
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)

is_break=False
for j in range(0, 2):
     if is_break:
         break
     start_url = f"https://www.mbauniverse.com/top-mba-colleges?page={j}"
     
     for k in range(1, 30):
         data={}
         if is_break:
             break
         driver.get(start_url)   
         data['collegeName'] = check_exists_by_xpath_text(driver, f'//*[@id="block-system-main"]/div/div/div[1]/table/tbody/tr[{k}]/td[3]/div/div[1]')

         collegeLink = check_exists_by_xpath_href(driver, f'//*[@id="block-system-main"]/div/div/div[1]/table/tbody/tr[{k}]/td[3]/div/div[1]/a')
         driver.get(collegeLink)
         
         data['collegeImg']=check_exists_by_xpath_src(driver,'//*[@id="block-views-colleges-block-3"]/div/div/div/div/div[1]/span/div/div[1]/a/img')
        
         data['collegeDesc'] = check_exists_by_xpath_text(driver, f'//*[@id="block-views-colleges-block-3"]')


         courseLink = check_exists_by_xpath_href(driver,'//*[@id="block-views-programs-block-2"]/div/div/div/div/div[1]/div/div[1]/div/div[1]/span/a')

         if(courseLink=="null"):
            courseLink=check_exists_by_xpath_href(driver,'//*[@id="block-views-programs-block-2"]/div/div/div/div/div/div[1]/span/a')

         driver.get(courseLink)
         data['courseInfo'] = check_exists_by_xpath_text(driver, '//*[@id="block-views-programs-block-5"]/div/div/div/div')
         
        # eligibility=check_exists_by_xpath_text(driver, '//*[@id="block-views-programs-block-6"]/div/div/div/div/div[1]/span/div[2]')
        # print(" Eligibilty\n"+eligibility)
         data['adminProcess'] = check_exists_by_xpath_text(driver, '//*[@id="block-views-programs-block-6"]/div/div/div/div/div[2]/span/div[2]/div[1]/span')

        # examDate=check_exists_by_xpath_text(driver,'//*[@id="block-views-programs-block-6"]/div/div/div/div/div[2]/span/div[2]/div[2]/span')
        # print(" Important Dates\n"+examDate)

         final_data.append(data)
         save(final_data)
         driver.back()
         driver.back()


     next_link = check_exists_by_xpath_href(driver,'//*[@id="block-system-main"]/div/div/div[2]/ul/li[3]/a')
     print(next_link)
     if(next_link == "null"):
        time.sleep(5)  
        driver.close() 
        is_break = True 
        # break
     else:
        driver.get(next_link)

time.sleep(5)
driver.close() 




