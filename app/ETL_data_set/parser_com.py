from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
import os
from com_mod_web_loc_tornado.read_cnf import read_cnf
import random
from sys import platform
import time
from selenium.webdriver.common.by import By
from dotmap import DotMap
#from pyvirtualdisplay import Display
#from xvfbwrapper import Xvfb

def init_drive(path,brauser,visual):
    """
    Инициализация драйвера
    :param brauser: Название браузеров GoogleChrome Firefox
    :return:
    """
    #full_path_chrom=os.path.abspath('chromedriver78_0_3904')
    # display = Display(visible=0, size=(800, 600))
    # display.start()
    # display = Xvfb()
    # display.start()
    full_path_fire = os.path.abspath('geckodriver')
    if brauser=="GoogleChrome":
        options_chr= webdriver.ChromeOptions()
        if visual!='v': options_chr.add_argument('headless')
        options_chr.add_argument('--no-sandbox')
        options_chr.add_argument('--disable-dev-shm-usage')
        #driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options_chr)
        #options_chr.binary_location='/home/al/com_prog/'
        # options_chr.add_experimental_option('prefs',{'geolocation': True})
        if platform == 'win32':
            driver = webdriver.Chrome(executable_path=path + "chromedriver", chrome_options=options_chr)
        else:
            driver = webdriver.Chrome(executable_path=path+"chromedriver_87",chrome_options=options_chr)
        #driver = webdriver.Chrome(path+"chromedriver_80",chrome_options=options_chr)
    if brauser == "Firefox":
        options_fier = webdriver.FirefoxOptions()
        options_fier.profile('/home/bigdata/.mozilla/firefox/')
        #options_fier.set_headless()
        #assert options_fier.headless
        driver = webdriver.Firefox(executable_path='geckodriver',options=options_fier)
        #driver = webdriver.Firefox(executable_path='geckodriver')
    return driver

def init_drivers(path,brauser,kol,vis):
    drivers=[]
    for i in range(kol):
        drivers.append(init_drive(path,brauser,vis))
    return drivers

# Класс получения адреса с серверов Яндекс. Сервера для запроса выбираются случайно из списка который загружается.
# Для того что бы использовать класс необходимо следующее:
# geoloc=Get_adress
# adress=geoloc.get_adress('ул. Пучкина, 12, Москва')
# adress.adress - Подробный адрес точки
# adress.coordinats - Координаты точки, если район то центр района (48.707067, 44.516948)
#


class Get_adress:
    def __init__(self):
        path_gl = os.getcwd()
        self.dict_adress={'adress':'','coordinats':''}
        self.driver=init_drivers(path_gl + '/com_mod_web_loc_tornado/','GoogleChrome',1,'n')[0]
        self.array_server =[]
        with open('servers_yandex.csv','r') as is_f:
            for line in is_f: self.array_server.append(line.strip())



    def get_adress(self,str_adres):
        self.driver.get(random.choice(self.array_server))
        pole_input = self.driver.find_element(By.XPATH, '//input[@class="input__control"]')
        str_adres=str_adres+'\n'
        pole_input.send_keys(str_adres)#.send_keys(webdriver.common.keys.Keys.ENTER())
        #pole_input.send_keys(Keys.ENTER)
        time.sleep(2)
        str_first = ''
        str_adress = ''
        str_coordinat = ''

        try:
            str_first = self.driver.find_element(By.XPATH, '//div[@class="card-title-view__wrapper"]//h1[@class="card-title-view__title"]').text + ','
        except Exception:
            str_first =''

        try:
            str_adress = self.driver.find_element(By.XPATH,
                                         '//div[@class="card-title-view__subtitle"]/div[@class="toponym-card-title-view__description"]').text
        except Exception:
            str_adress=''

        try:
            str_coordinat = self.driver.find_element(By.XPATH,
                                            '//div[@class="card-title-view__subtitle"]//div[@class="clipboard__action-wrapper _inline _view_primary"]').text
        except Exception:
            str_coordinat=''

        self.dict_adress['adress']=str_first+str_adress
        self.dict_adress['coordinats'] = str_coordinat
        my_dict=DotMap(self.dict_adress)
        return my_dict
