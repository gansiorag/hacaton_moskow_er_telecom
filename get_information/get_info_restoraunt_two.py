"""
This module get all info about restaurants from https://www.afisha.ru/msk/restaurants/restaurant_list/?view=list

author Gansior A.G. gansior@gansior.ru
"""

import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from app.drivers.init_drevers import init_drivers
import time

def get_all_href(driver):
    rezult_file=open('../href_restoraunts_2.csv', 'a')
    driver.get('https://www.afisha.ru/msk/restaurants/restaurant_list/')
    kol_all = 0
    kol_tec = 1
    while True:
       print('kol_all ---> ', kol_all)
       kol_all = kol_tec
       butt = driver.find_element_by_xpath('//div[@class="show-more_button j-show-more-button"]/a')
       #butt = driver.find_element_by_class_name("show-more_button j-show-more-button")
       # bott = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, '//div[@class="show-more_button j-show-more-button"]/a')))
       butt.click()
       driver.implicitly_wait(20)
       #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       #time.sleep(6)
       all_page_a = driver.find_elements_by_xpath('//li[@class="list_item"]')
       kol_tec = len(all_page_a)
       print(len(all_page_a))
       print('kol_tec ---> ', kol_tec)
       # for href in all_page_a[0::2]:
       #     print(href.text, href.get_attribute('href'), sep=' --> ')
       #     rezult_file.write(href.text +';' +  href.get_attribute('href') + '\n')
       # try:
       #     butt = driver.find_element_by_xpath('//li[@class="next-arrow"]/a')
       #     butt.click()
       #     time.sleep(1)
       # except Exception:
       #     my_key = False

def usulay_page(driver,all_rest, is_list):
    driver.find_element_by_xpath('//div[@class="read-more all-props-trigger-wrap"]').click()
    base = driver.find_element_by_xpath('//div[@id="props"]')
    params = base.find_elements_by_xpath('./div[@class="prop"]')
    all_rest[is_list[0]] = {}

    for div in params:
        name = div.find_element_by_xpath('./div[@class="name"]').text
        print(name)
        if 'Телефон' not in name:  # or (name not in 'Телефон:'):
            if name == 'Адрес:':
                value = div.find_element_by_xpath('./div[@class="value address-wrap"]').text
            elif name == 'Парковка:':
                try:
                    value = div.find_element_by_xpath('./div[@class="value parking "]').text
                except Exception:
                    value = "Парковки нет"
            else:
                value = div.find_element_by_xpath('./div[@class="value"]').text
            all_rest[is_list[0]][name] = value

    base2 = base.find_element_by_xpath('./div[@class="more-props"]')
    params = base2.find_elements_by_xpath('./div[@class="prop"]')
    for div in params:
        name = div.find_element_by_xpath('./div[@class="name"]').text.replace('\n', ' ')
        print(name)
        value = div.find_element_by_xpath('./div[@class="value"]').text
        all_rest[is_list[0]][name] = value


def get_all_param(driver):
    all_rest ={}
    k=0
    with open('../href_restoraunts_1.csv', 'r') as is_f:
        for line in is_f:
            k +=1
            print(k)
            if k>742:
                is_list = line.strip().split(';')
                driver.get(is_list[1])
                usulay_page(driver, all_rest, is_list)
                pprint.pprint(all_rest)


if __name__ == '__main__':
    driver = init_drivers(vis=True)[0]
    get_all_href(driver)
    #get_all_param(driver)