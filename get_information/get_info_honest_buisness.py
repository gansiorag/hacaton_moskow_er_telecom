from app.drivers.init_drevers import init_drivers
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome(r'C:\Users\Vbano\PycharmProjects\hacaton_moskow_er_telecom\app\drivers\chromedriver\chromedriver_89')
    driver.get('https://zachestnyibiznes.ru/company/ul/1047796535874_7723517121_AGAPE')
