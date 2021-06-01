"""
This module collection of scripts to help

Author Gansior A. mail - gansior@gansior.ru tel - +79173383804

"""
from geopy import distance
import math

def proga():
    print(round(distance.GeodesicDistance([55.755,37.60176], [55.755,37.600]).m,0))

def get_array_borders_squere(hi_point = [55.7744, 37.580],  low_point = [55.7294, 37.652], leng_side = 100):
    kol_sqrt_width = int(round(distance.GeodesicDistance([hi_point[0], 0.0], [low_point[0], 0.0]).m,0)/leng_side)
    kol_sqrt_long = int(round(distance.GeodesicDistance([0.0, hi_point[1]], [0.0, low_point[1]]).m,0)/(leng_side*1.6))

    print(kol_sqrt_width)
    print(kol_sqrt_long)
    koef_lend =leng_side/100.0
    print(koef_lend)
    array_sqrt = []
    for ww in range(0, kol_sqrt_width):
        for ll in range(0, kol_sqrt_long):
            # print(round(distance.GeodesicDistance([hi_point[0]+0.0009*ww*koef_lend,
            #                                        hi_point[1]+0.0016*ll*koef_lend],
            #                                        [hi_point[0] + 0.0009 * (ww + 1)*koef_lend,
            #                                         hi_point[1] + 0.0016 * (ll+1)*koef_lend]).m, 0))
            array_sqrt.append([[hi_point[0] - 0.0009*ww*koef_lend, hi_point[1] - 0.0016*ll*koef_lend],
                              [hi_point[0] - 0.0009 * (ww + 1) * koef_lend, hi_point[1] - 0.0016 * (ll + 1) * koef_lend]]
                              )
    return kol_sqrt_width, kol_sqrt_long, koef_lend, array_sqrt


class One_pix():
    def __init__(self, dict_param: dict):
        sqrt_pix = dict_param['coord_sqrt']


class Work_with_One_pix():
    def __init__(self, dict_arry_One_pix:dict):
        pass

def get_array_objects(hi_point = [55.7744, 37.580],  low_point = [55.7294, 37.652], name_files='lll.csv'):
    with open(name_files, 'r') as is_f:
        pass



if __name__ == '__main__':
    proga()
    hi_point = [55.7744, 37.580]
    low_point = [55.7294, 37.652]
    leng_side = 100
    array_objects = get_array_objects(hi_point, low_point,
                                      '/home/al/PycharmProjects/hacaton_moskow_er_telecom/data_set/theatres.csv')
    kol_sqrt_width, kol_sqrt_long, koef_lend, array_sqrt = \
        get_array_borders_squere(hi_point = hi_point,  low_point = low_point, leng_side = leng_side)
    # for pix in array_sqrt:
    #     dd = {''}
    #     new_pix = One_pix({'coord_sqrt':pix})

