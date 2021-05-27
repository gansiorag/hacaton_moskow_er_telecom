"""
This module make

author Gansior A.G. gansior@gansior.ru
"""
from drivers.init_drevers import init_drivers
import time

def proga():
    pass

if __name__ == '__main__':
    driver = init_drivers()[0]
    driver.get('https://yandex.ru/')
    allh1 = driver.find_element_by_xpath('//input[@class="input__control input__input mini-suggest__input"]')
    allh1.send_keys('Где находиться река Волга?\n')
    time.sleep(5)
    #all_rezult = driver.find_elements_by_xpath('//ul[@class="serp-list serp-list_left_yes"]//li')
    rr ='//ul[@class="serp-list serp-list_left_yes"]//a[@class="Link Link_theme_outer Path-Item link path__item i-bem link_js_inited"]'
    all_rezult = driver.find_elements_by_xpath(rr)
    print(len(all_rezult))
    for tt in all_rezult:
        print(tt.get_attribute('href'))


