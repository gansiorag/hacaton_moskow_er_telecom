"""
This module collection of scripts to help

Author Gansior A. mail - gansior@gansior.ru tel - +79173383804

"""
from geopy import distance
import math

def proga():
    print(round(distance.GeodesicDistance([55.755,37.60176], [55.755,37.600]).m,0))

def get_array_borders_squere(hi_point = [55.7744, 37.580],  low_point = [55.7294, 37.66], leng_side = 100):
    width = abs(hi_point[0] - low_point[0])
    long = abs(hi_point[1] - low_point[1])
    print(width)
    print(long)
    kol_sqrt = int(width/0.001)
    koef_lend = leng_side/100.0
    print(kol_sqrt)
    for ww in range(0, kol_sqrt):
        for ll in range(0, kol_sqrt):
            print(round(distance.GeodesicDistance([hi_point[0]+0.0009*ww*koef_lend,
                                                   hi_point[1]+0.0016*ll*koef_lend],
                                                   [hi_point[0] + 0.0009 * (ww + 1)*koef_lend,
                                                    hi_point[1] + 0.0016 * (ll+1)*koef_lend]).m, 0))






if __name__ == '__main__':
    proga()
    get_array_borders_squere()

