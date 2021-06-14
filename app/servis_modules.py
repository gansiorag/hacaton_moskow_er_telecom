"""
This module collection of scripts to help

Author Gansior A. mail - gansior@gansior.ru, tel - +79173383804

"""

from geopy import distance
import math
import os
from pprint import pprint

try:
    from app.work_with_data_set import Data_set
except Exception:
    from work_with_data_set import Data_set

try:
    from app.class_Onix import One_pix
except Exception:
    from class_Onix import One_pix


def get_end_coord_rectangle(hi_point = [55.7744, 37.580],  low_point = [55.7294, 37.652], leng_side = 100):

    # рассчет широты нижней точки
    high = round(distance.GeodesicDistance([hi_point[0], 0], [low_point[0], 0]).m, 0)
    # print('high = ', high)
    # print('leng_side = ', leng_side)
    koef_high_m = int(high/leng_side)
    #print('koef_high_m =', koef_high_m)
    new_high = koef_high_m*leng_side
    end_high = 0.0
    if new_high<high : koef_high_m = koef_high_m + 1
    koef_high = koef_high_m*leng_side/100
    end_with_coordinate = hi_point[0] -  0.0009 *koef_high

    # рассчет долготы нижней точки
    long = round(distance.GeodesicDistance([0, hi_point[1]], [0, low_point[1]]).m, 0)
    #print('long = ', long)
    koef_long_m = int(long / (leng_side*1.6))
    #print('koef_long_m = ',koef_long_m)
    new_long = koef_long_m * leng_side
    end_long = 0.0
    if new_long < long: koef_long_m = koef_long_m + 1
    koef_long = koef_long_m*leng_side / 100
    end_long_coordinate = hi_point[1] + 0.0016 * koef_long

    #print(end_with_coordinate, end_long_coordinate)
    return [end_with_coordinate, end_long_coordinate]

def get_array_borders_squere(hi_point = [55.7744, 37.580],  low_point = [55.7294, 37.652], leng_side = 100):
    length_high = round(distance.GeodesicDistance([hi_point[0], 0.0], [low_point[0], 0.0]).m,0)
    kol_sqrt_width = int(length_high/leng_side)
    if kol_sqrt_width*leng_side < length_high: kol_sqrt_width = kol_sqrt_width + 1

    length_longer = round(distance.GeodesicDistance([0.0, hi_point[1]], [0.0, low_point[1]]).m,0)
    kol_sqrt_long = int(length_longer/(leng_side*1.6))
    if kol_sqrt_long*leng_side < length_longer: kol_sqrt_long = kol_sqrt_long +1

    #print(kol_sqrt_width)
    #print(kol_sqrt_long)
    koef_lend =leng_side/100.0
    #print(koef_lend)
    array_sqrt = []
    for ww in range(0, kol_sqrt_width):
        for ll in range(0, kol_sqrt_long):
            # print(round(distance.GeodesicDistance([hi_point[0]+0.0009*ww*koef_lend,
            #                                        hi_point[1]+0.0016*ll*koef_lend],
            #                                        [hi_point[0] + 0.0009 * (ww + 1)*koef_lend,
            #                                         hi_point[1] + 0.0016 * (ll+1)*koef_lend]).m, 0))
            array_sqrt.append([[hi_point[0] - 0.0009*ww*koef_lend, hi_point[1] + 0.0016 * ll * koef_lend],
                              [hi_point[0] - 0.0009 * (ww + 1) * koef_lend, hi_point[1] + 0.0016*(ll+1)*koef_lend,]]
                              )
    return kol_sqrt_width, kol_sqrt_long, koef_lend, array_sqrt




class Work_with_One_pix():
    """
    class work with One_pix

    """
    def __init__(self, dict_arry_One_pix:dict):
        self.Base_array = dict_arry_One_pix
        #print(self.Base_array)
        #self.array_sqrt = array_sqrt
        #print(self.array_sqrt)
        #self.array_data_sqrt = self.divide_data_sqrt()

    def divide_data_sqrt(self, array_sqrt, list_obj):
        """
        create array sqrts with objects
        :return:
        """
        arr = []
        for sqrt in array_sqrt:
            arr.append(self.get_data_sqrt(sqrt, list_obj))
        return arr

    def get_data_sqrt(self, sqrt, list_obj):
        """
        get all type objects in sqrt
        :param sqrt: coordinate sqrt = [[start point, end point],[start point, end point]]
        :return: list with number objects on type [10,20,0,33,325,66,58]
        """
        array_obj = {}
        for type_obj in self.Base_array:
            if (type_obj in list_obj) and (type_obj !='data_wifi'):

                if type_obj not in ['data_wifi', 'activity_people']:
                    kol_obj = 0
                    #print(type_obj)
                    #print(self.Base_array[type_obj])
                    for obbj in self.Base_array[type_obj]:
                            if ((sqrt[0][0] >= obbj['ltt']) and (sqrt[1][0] <= obbj['ltt'])) and\
                               ((sqrt[0][1] <= obbj['lnt']) and (sqrt[1][1] >= obbj['lnt'])) :
                                kol_obj += 1
                    array_obj[type_obj] = kol_obj
                if type_obj in ['data_wifi', 'activity_people']:
                    #print(self.Base_array[type_obj][0]['nabor'])
                    data_day_20 = self.Base_array[type_obj][0]['nabor']
                    servis_data = data_day_20.loc[(data_day_20['ltt'].astype(float) <= sqrt[0][0]) &
                                                  (data_day_20['ltt'].astype(float) >= sqrt[1][0]) &
                                                  (data_day_20['lnt'].astype(float) >= sqrt[0][1]) &
                                                  (data_day_20['lnt'].astype(float) <= sqrt[1][1])]

                    array_obj['kol_point_wifi'] = len(servis_data['ap_mac'].unique())
                    array_obj['kol_devices'] = len(servis_data['device_id'].unique())
                    array_obj['kol_events'] = len(servis_data['ltt'])
                    if (array_obj['kol_point_wifi'] > 0 and
                            array_obj['kol_devices'] > 0):
                        array_obj['activity_people'] = round(array_obj['kol_events'] /
                                                        (array_obj['kol_point_wifi'] *
                                                         array_obj['kol_devices']), 3)
        return array_obj



# test part

if __name__ == '__main__':
    #proga()
    #55.754311° 37.522732°
    #55.701605° 37.70619°
    # start_width = 55.7744
    # start_long = 37.580
    # end_width = 55.7294
    # end_long = 37.652
    start_width = 55.754311
    start_long = 37.522732
    end_width = 55.701605
    end_long = 37.70619

    zoom = 12 # start zoom

    # this coordinates center rectangle
    pcc = (start_long + end_long)/2
    lcc = (start_width + end_width)/2
    hi_point = [ start_width, start_long]
    low_point = [end_width, end_long]
    print('low_point 1 = ', low_point)
    leng_side = 3000
    low_point = get_end_coord_rectangle(hi_point,low_point,leng_side)
    print('low_point 2 = ', low_point)

    param = {'coord_pix':[[pcc, lcc], hi_point,low_point]}
    main_reactange = One_pix(param)
    #pprint(main_reactange.array_objects_pix['food'])
    print('len food = ',len(main_reactange.array_objects_pix['food']))
    #pprint(main_reactange.array_objects_pix['food'])
    # print('len intercepting_parking = ', len(main_reactange.array_objects_pix['intercepting_parking']))
    # print('len theaters = ',len(main_reactange.array_objects_pix['theaters']))
    # print('len paid_parking = ', len(main_reactange.array_objects_pix['paid_parking']))
    # print('len closed_paid_parking = ', len(main_reactange.array_objects_pix['closed_paid_parking']))
    # print('len cinemas = ', len(main_reactange.array_objects_pix['cinemas']))
    # print('len circus = ', len(main_reactange.array_objects_pix['circus']))
    # print('len concert_halls = ', len(main_reactange.array_objects_pix['concert_halls']))
    # print('len museums = ', len(main_reactange.array_objects_pix['museums']))
    # # print('len monuments = ', len(main_reactange.array_objects_pix['monuments']))
    # print('len education = ', len(main_reactange.array_objects_pix['education']))
    kol_sqrt_width, kol_sqrt_long, koef_lend, array_sqrt = get_array_borders_squere(hi_point=hi_point,
                                                                                    low_point=low_point,
                                                                                    leng_side=leng_side)

    pprint(array_sqrt)
    print(kol_sqrt_width, kol_sqrt_long)
    work_array =  Work_with_One_pix(main_reactange.array_objects_pix)
    rezult = work_array.divide_data_sqrt(array_sqrt)
    """
    atelier': 18,
  'bathing_services': 0,
  'builts'
  'cinemas': 1,
  'circus': 0,
  'closed_paid_parking': 0,
  'comprehensive_domestic_services': 20,
  'concert_halls': 0,
  'data_wifi': 6,
  'dry_cleanings_dyeing': 5,
  'education': 9,
  'food': 506,
  'furniture_services': 1,
  'hairdressers': 120,
  'home_electronics_services': 14,
  'intercepting_parking': 0,
  'jewelry_services': 5,
  'laundries': 0,
  'metal_services': 6,
  'metro_exits': 9,
  'museums': 6,
  'other_domestic_services': 2,
  'paid_parking': 377,
  'parks': 0,
  'pawnshops': 3,
  'photo_studios': 22,
  'rental_services': 1,
  'ritual_services': 0,
  'saunas': 3,
  'self_service_dry_cleaners': 2,
  'self_service_laundries': 1,
  'shoe_services': 6,
  'theaters': 6,
  'watch_services': 6"""
    for dd in rezult:
        pprint(dd['hairdressers'])
        #print(dd['comprehensive_domestic_services'])
    #pprint(work_array.divide_data_sqrt(array_sqrt))

