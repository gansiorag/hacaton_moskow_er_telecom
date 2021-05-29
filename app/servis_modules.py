"""
This module make

Author Gansior A. mail - gansior@gansior.ru tel - +79173383804
"""
from geopy import distance

def proga():
    print(round(distance.GeodesicDistance([55.755,37.60176], [55.755,37.600]).m,0))




if __name__ == '__main__':
    proga()

