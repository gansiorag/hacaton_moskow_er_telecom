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


def get_end_coord_rectangle(hi_point = [55.7744, 37.580],  low_point = [55.7294, 37.652], leng_side = 100):

    # рассчет широты нижней точки
    high = round(distance.GeodesicDistance([hi_point[0], 0], [low_point[0], 0]).m, 0)
    print('high = ', high)
    print('leng_side = ', leng_side)
    koef_high_m = int(high/leng_side)
    print('koef_high_m =', koef_high_m)
    new_high = koef_high_m*leng_side
    end_high = 0.0
    if new_high<high : koef_high_m = koef_high_m + 1
    koef_high = koef_high_m*leng_side/100
    end_with_coordinate = hi_point[0] -  0.0009 *koef_high

    # рассчет долготы нижней точки
    long = round(distance.GeodesicDistance([0, hi_point[1]], [0, low_point[1]]).m, 0)
    print('long = ', long)
    koef_long_m = int(long / (leng_side*1.6))
    print('koef_long_m = ',koef_long_m)
    new_long = koef_long_m * leng_side
    end_long = 0.0
    if new_long < long: koef_long_m = koef_long_m + 1
    koef_long = koef_long_m*leng_side / 100
    end_long_coordinate = hi_point[1] + 0.0016 * koef_long

    print(end_with_coordinate, end_long_coordinate)
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



class One_pix():
    def __init__(self, dict_param: dict):
        self.center_pix = dict_param['coord_pix'][0]
        self.hi_point_pix = dict_param['coord_pix'][1]
        self.low_point_pix = dict_param['coord_pix'][2]
        print(self.hi_point_pix)
        print(self.low_point_pix)
        path = os.path.abspath(os.getcwd()).split('hacaton_moskow_er_telecom')[0] + 'hacaton_moskow_er_telecom/app/'
        print('path- ',path)
        self.array_type_objects={'theaters':{'path': path + 'data_set/theatres.csv',
                                             'sep': ';'},
                                 'food':{'path': path + 'data_set/общепит_data-4275-2021-06-01.csv',
                                         'sep':'^'},
                                 'intercepting_parking':{'path': path + 'data_set/парковки/intercepting_parking.csv',
                                         'sep':';'},
                                 'paid_parking': {'path': path + 'data_set/парковки/paid_parking.csv',
                                         'sep':';'},
                                 'closed_paid_parking': {'path': path + 'data_set/парковки/closed_paid_parking.csv',
                                         'sep':';'},
                                 'cinemas': {'path': path + 'data_set/cinemas.csv',
                                         'sep':';'},
                                 'circus': {'path': path + 'data_set/circus.csv',
                                         'sep':';'},
                                 'concert_halls': {'path': path + 'data_set/concertHalls.csv',
                                         'sep':';'},
                                 'museums': {'path': path + 'data_set/museums.csv',
                                         'sep':';'},
                                 'monuments': {'path': path + 'data_set/monuments.csv',
                                         'sep':';'},
                                 'education': {'path': path + 'data_set/education.csv',
                                         'sep':';'},
                                 'parks': {'path': path + 'data_set/parks.csv',
                                         'sep':';'},
                                 'metro_exits': {'path': path + 'data_set/metro_exits.csv',
                                         'sep':';'},
                                 }
        self.array_objects_pix = {'theaters': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'theaters',
                                                                     self.array_type_objects['theaters']['path']),
                                  'food': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'food',
                                                                     self.array_type_objects['food']['path']),
                                  'intercepting_parking': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'intercepting_parking',
                                                                     self.array_type_objects['intercepting_parking']['path']),
                                  'paid_parking': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'paid_parking',
                                                                     self.array_type_objects['paid_parking']['path']),
                                  'closed_paid_parking': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'closed_paid_parking',
                                                                     self.array_type_objects['closed_paid_parking']['path']),
                                  'cinemas': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'cinemas',
                                                                     self.array_type_objects['cinemas']['path']),
                                  'circus': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'circus',
                                                                     self.array_type_objects['circus']['path']),
                                  'concert_halls': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'concert_halls',
                                                                     self.array_type_objects['concert_halls']['path']),
                                  'museums': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'museums',
                                                                     self.array_type_objects['museums']['path']),
                                  # 'monuments': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                  #                                    self.low_point_pix,
                                  #                                    'monuments',
                                  #                                    self.array_type_objects['monuments']['path']),
                                  'education': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'education',
                                                                     self.array_type_objects['education']['path']),
                                  'parks': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'education',
                                                                     self.array_type_objects['parks']['path']),
                                  'metro_exits': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'metro_exits',
                                                                     self.array_type_objects['metro_exits']['path'])
                                  }


    def get_array_objects_from_file_data_set(self, hi_point = [55.7744, 37.580],
                          low_point = [55.7294, 37.652],
                          name_array = 'nonsens',
                          name_files = 'lll.csv') -> list:
        array_def = []
        with open(name_files, 'r') as is_f:
            k = 0
            for line in is_f:
                k += 1
                analiz = Data_set(line,
                    self.array_type_objects[name_array]['sep'],
                    self.hi_point_pix,
                    self.low_point_pix)
                if name_array =='theaters' :
                    ddd = analiz.theatres()
                    if ddd: array_def.append(ddd)
                if name_array =='food' and k!= 1:
                    ddd = analiz.food()
                    if ddd: array_def.append(ddd)
                if name_array =='intercepting_parking':
                    ddd = analiz.intercepting_parking()
                    if ddd: array_def.append(ddd)
                if name_array =='paid_parking':
                    ddd = analiz.paid_parking()
                    if ddd: array_def.append(ddd)
                if name_array =='closed_paid_parking':
                    ddd = analiz.closed_paid_parking()
                    if ddd: array_def.append(ddd)
                if name_array =='cinemas':
                    ddd = analiz.cinemas()
                    if ddd: array_def.append(ddd)
                if name_array =='circus':
                    ddd = analiz.circus()
                    if ddd: array_def.append(ddd)
                if name_array =='concert_halls':
                    ddd = analiz.concert_halls()
                    if ddd: array_def.append(ddd)
                if name_array =='museums':
                    ddd = analiz.museums()
                    if ddd: array_def.append(ddd)
                if name_array =='monuments':
                    ddd = analiz.monuments()
                    if ddd: array_def.append(ddd)
                if name_array =='education':
                    ddd = analiz.education()
                    if ddd: array_def.append(ddd)
                if name_array =='parks':
                    ddd = analiz.parks()
                    if ddd: array_def.append(ddd)
                if name_array =='metro_exits':
                    ddd = analiz.metro_exits()
                    if ddd: array_def.append(ddd)
        return array_def


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

    def divide_data_sqrt(self, array_sqrt):
        """
        create array sqrts with objects
        :return:
        """
        arr = []
        for sqrt in array_sqrt:
            arr.append(self.get_data_sqrt(sqrt))
        return arr

    def get_data_sqrt(self, sqrt):
        """
        get all type objects in sqrt
        :param sqrt: coordinate sqrt = [[start point, end point],[start point, end point]]
        :return: list with number objects on type [10,20,0,33,325,66,58]
        """
        array_obj = []
        for type_obj in self.Base_array:
            kol_obj = 0
            #print(type_obj)
            for obbj in self.Base_array[type_obj]:
                    if ((sqrt[0][0] >= obbj['ltt']) and (sqrt[1][0] <= obbj['ltt'])) and\
                       ((sqrt[0][1] <= obbj['lnt']) and (sqrt[1][1] >= obbj['lnt'])) :
                        kol_obj += 1
            array_obj.append(kol_obj)
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
    pprint(work_array.divide_data_sqrt(array_sqrt))

