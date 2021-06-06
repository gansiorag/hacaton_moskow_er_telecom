"""
This module collection of scripts to help

Author Gansior A. mail - gansior@gansior.ru, tel - +79173383804

"""

from geopy import distance
import math
from pprint import pprint
from work_with_data_set import Data_set

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
        self.center_pix = dict_param['coord_pix'][0]
        self.hi_point_pix = dict_param['coord_pix'][1]
        self.low_point_pix = dict_param['coord_pix'][2]
        print(self.hi_point_pix)
        self.array_type_objects={'theaters':{'path':'app/data_set/theatres.csv', 
                                             'sep': ';'},
                                 'food':{'path':'app/data_set/общепит_data-4275-2021-06-01.csv',
                                         'sep':'^'}
                                 
                                 }
        self.array_objects_pix = {'theaters': self.get_array_objects(self.hi_point_pix, 
                                                                     self.low_point_pix, 
                                                                     'theaters', 
                                                                     self.array_type_objects['theaters']['path']),
                                  'food': self.get_array_objects(self.hi_point_pix, 
                                                                     self.low_point_pix, 
                                                                     'food', 
                                                                     self.array_type_objects['food']['path'])
                                  }
        
    
    def get_array_objects(self, hi_point = [55.7744, 37.580],  
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
        return array_def
    

class Work_with_One_pix():
    def __init__(self, dict_arry_One_pix:dict):
        pass



# test part

if __name__ == '__main__':
    #proga()
    start_width = 55.7744
    start_long = 37.580
    end_width = 55.7294
    end_long = 37.652

    zoom = 12 # start zoom

    # this coordinates center rectangle
    pcc = (start_long + end_long)/2
    lcc = (start_width + end_width)/2
    hi_point = [ start_width, start_long]
    low_point = [end_width, end_long]
    leng_side = 500
    param = {'coord_pix':[[pcc, lcc], hi_point,low_point]}
    main_reactange = One_pix(param)
    pprint(main_reactange.array_objects_pix['food'])
    print('len = ',len(main_reactange.array_objects_pix['food']))
