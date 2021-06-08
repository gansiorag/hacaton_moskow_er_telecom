from selenium import webdriver
import os

def init_drive(brauser, vision = False):
    """
    Инициализация драйвера
    :param brauser: Название браузеров GoogleChrome Firefox
    :return:
    """
    path = os.getcwd().split('/drivers/')
    full_path_chrom=path[0]  + '/drivers/chromedriver/chromedriver_89'
    full_path_fire = os.path.abspath('geckodriver')
    print(full_path_chrom)

    if brauser=="GoogleChrome":
        options_chr= webdriver.ChromeOptions()
        if not vision :
            options_chr.add_argument('headless')
        #options_chr.add_experimental_option('prefs',{'geolocation': True})
        driver = webdriver.Chrome(full_path_chrom,chrome_options=options_chr)

    if brauser == "Firefox":
        options_fier = webdriver.FirefoxOptions()
        options_fier.profile('/home/al/.mozilla/firefox/yysvauj1.default-release')
        # options_fier.set_headless()
        # assert options_fier.headless
        driver = webdriver.Firefox(executable_path=full_path_fire,options=options_fier)

    return driver


def init_drivers(brauser="GoogleChrome", kol=1, vis = False):
    drivers=[]
    for i in range(kol):
        drivers.append(init_drive(brauser, vis))
    return drivers

# def geoloc():
#     # access_token = '123456789abc'
#     # handler = ipinfo.getHandler(access_token)
#     # details = handler.getDetails()
#     # print(details.city)
#     import socket
#     import fcntl
#     import struct
#     name = socket.gethostname()
#     id_address = socket.gethostbyname(name)
#     print("id_address = {0}".format(id_address))
#     ifname='eth0'
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.connect(("8.8.8.8", 80))
#     print(s.getsockname()[0])
#     print(s.getsockname()[1])
#     from subprocess import check_output
#     ips = check_output(['hostname', '--all-ip-addresses'])
#     print(ips)
#     f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
#     print('your_ip =', f.read())
#     ipv4 = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
#     ipv6 = os.popen('ip addr show eth0').read().split("inet6 ")[1].split("/")[0]
#     print('ipv4 = ',ipv4)
#     print('ipv6 = ', ipv6)


#
# import pymysql
# def config_mysql():
#     con = pymysql.connect('localhost', 'root', 'GANsiBR586!', 'helpify_ml')
#     cur = con.cursor()
#     return con,cur

# block test
if __name__ == "__main__":
    driver = init_drivers()[0]
    driver.get('https://www.google.com')
    print("Without visiual")
    driver.close
    driver = init_drivers(vis=True)[0]
    driver.get('https://www.google.com')

