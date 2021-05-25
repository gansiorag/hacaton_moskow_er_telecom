from drivers.init_drevers import init_drivers

def get_all_href(driver):
   driver.get('https://www.restoran.ru/msk/catalog/restaurants/all/')
   all_page_a = driver.find_elements_by_xpath('//div[@class="place-about"]/a')
   print(len(all_page_a))
   for href in all_page_a:
       print(href.text, href.get_attribute('href'), sep=' --> ')


if __name__ == '__main__':
    driver = init_drivers()[0]
    get_all_href(driver)
