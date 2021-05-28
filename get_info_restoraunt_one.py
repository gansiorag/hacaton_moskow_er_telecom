import pprint
import json

from drivers.init_drevers import init_drivers
import time
def get_all_href(driver):
    rezult_file=open('href_restoraunts_1.csv', 'a')
    driver.get('https://www.restoran.ru/msk/catalog/restaurants/all/')
    my_key = True
    kol = 0
    while my_key :
       kol +=1
       print(kol)
       all_page_a = driver.find_elements_by_xpath('//div[@class="place-about"]/a')
       print(len(all_page_a))
       for href in all_page_a[0::2]:
           print(href.text, href.get_attribute('href'), sep=' --> ')
           rezult_file.write(href.text +';' +  href.get_attribute('href') + '\n')
       try:
           butt = driver.find_element_by_xpath('//li[@class="next-arrow"]/a')
           butt.click()
           time.sleep(1)
       except Exception:
           my_key = False

def usulay_page(driver, is_list):
    all_rest = {}
    driver.find_element_by_xpath('//div[@class="read-more all-props-trigger-wrap"]').click()
    base = driver.find_element_by_xpath('//div[@id="props"]')
    params = base.find_elements_by_xpath('./div[@class="prop"]')
    all_rest[is_list[0]] = {}

    for div in params:
        name = div.find_element_by_xpath('./div[@class="name"]').text
        #print(name)
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
        #print(name)
        value = div.find_element_by_xpath('./div[@class="value"]').text
        all_rest[is_list[0]][name] = value
    return all_rest

def restoraut_net(driver, is_list):
    all_resttt = []
    level_one =driver.find_elements_by_xpath('//div[@class="item active"]/div[@class="contact props"]')
    text_level = 0
    for base in level_one:
        one_rest = {}
        text_level +=1
        params = base.find_elements_by_xpath('./div[@class="prop"]')
        one_rest [is_list[0]]={}
        metro = base.find_element_by_xpath('./div[@class="prop wsubway"]')
        one_rest[is_list[0]][metro.find_element_by_xpath('./div[@class="name"]').text] = \
                            metro.find_element_by_xpath('./div[@class="value"]').text
        for itt in params:
            one_rest[is_list[0]][itt.find_element_by_xpath('./div[@class="name"]').text] = \
                itt.find_element_by_xpath('./div[@class="value"]').text
            #print(itt.find_element_by_xpath('./div[@class="name"]').text,
            #      itt.find_element_by_xpath('./div[@class="value"]').text, sep=' -->> ' )
        #print('-----------------')
        all_resttt.append(one_rest)
    return all_resttt


def get_all_param(driver):
    all_rest =[]
    k=0

    with open('href_restoraunts_1.csv', 'r') as is_f:
        for line in is_f:
            k +=1
            print(k)
            is_list = line.strip().split(';')
            driver.get(is_list[1])
            try:
                ittem = usulay_page(driver, is_list)
                all_rest.append(ittem)
            except Exception:
                ittem = restoraut_net(driver, is_list)
                all_rest += ittem
            #pprint.pprint(all_rest)

    with open('all_rest.csv', 'a') as rez_f:
        for itt in all_rest:
            rez_f.write(json.dumps(itt, ensure_ascii=False)+'\n')




if __name__ == '__main__':
    driver = init_drivers()[0]
    #get_all_href(driver)
    get_all_param(driver)
