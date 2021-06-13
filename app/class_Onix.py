"""
This module make

Author Gansior A. mail - gansior@gansior.ru tel - +79173383804
"""
import os
try:
    from app.work_with_data_set import Data_set
except Exception:
    from work_with_data_set import Data_set

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
                                 'atelier': {'path': path + 'data_set/domestic_services/atelier.csv',
                                         'sep':';'},
                                 'bathing_services': {'path': path + 'data_set/domestic_services/bathing_services.csv',
                                         'sep':';'},
                                 'comprehensive_domestic_services': {'path': path + 'data_set/domestic_services/comprehensive_domestic_services.csv',
                                         'sep':';'},
                                 'dry_cleanings_dyeing': {'path': path + 'data_set/domestic_services/dry_cleanings_dyeing.csv',
                                         'sep':';'},
                                 'furniture_services': {'path': path + 'data_set/domestic_services/furniture_services.csv',
                                         'sep':';'},
                                 'hairdressers': {'path': path + 'data_set/domestic_services/hairdressers.csv',
                                         'sep':';'},
                                 'home_electronics_services': {'path': path + 'data_set/domestic_services/home_electronics_services.csv',
                                         'sep':';'},
                                 'jewelry_services': {'path': path + 'data_set/domestic_services/jewelry_services.csv',
                                         'sep':';'},
                                 'laundries': {'path': path + 'data_set/domestic_services/laundries.csv',
                                         'sep':';'},
                                 'metal_services': {'path': path + 'data_set/domestic_services/metal_services.csv',
                                         'sep':';'},
                                 'other_domestic_services': {'path': path + 'data_set/domestic_services/other_domestic_services.csv',
                                         'sep':';'},
                                 'pawnshops': {'path': path + 'data_set/domestic_services/pawnshops.csv',
                                         'sep':';'},
                                 'photo_studios': {'path': path + 'data_set/domestic_services/photo_studios.csv',
                                         'sep':';'},
                                 'rental_services': {'path': path + 'data_set/domestic_services/rental_services.csv',
                                         'sep':';'},
                                 'ritual_services': {'path': path + 'data_set/domestic_services/ritual_services.csv',
                                         'sep':';'},
                                 'saunas': {'path': path + 'data_set/domestic_services/saunas.csv',
                                         'sep':';'},
                                 'self_service_dry_cleaners': {'path': path + 'data_set/domestic_services/self_service_dry_cleaners.csv',
                                         'sep':';'},
                                 'self_service_laundries': {'path': path + 'data_set/domestic_services/self_service_laundries.csv',
                                         'sep':';'},
                                 'shoe_services': {'path': path + 'data_set/domestic_services/shoe_services.csv',
                                         'sep':';'},
                                 'watch_services': {'path': path + 'data_set/domestic_services/watch_services.csv',
                                         'sep':';'},
                                 'data_wifi': {'path': path + 'data_set/data_day_2021_03_20.csv',
                                                    'sep': '^'},
                                 'builds': {'path': path + 'data_set/builds.csv',
                                                    'sep': '^'},
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
                                                                     self.array_type_objects['metro_exits']['path']),
                                  'atelier': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'atelier',
                                                                     self.array_type_objects['atelier']['path']),
                                  'bathing_services': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'bathing_services',
                                                                     self.array_type_objects['bathing_services']['path']),
                                  'comprehensive_domestic_services': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'comprehensive_domestic_services',
                                                                     self.array_type_objects['comprehensive_domestic_services']['path']),
                                  'dry_cleanings_dyeing': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'dry_cleanings_dyeing',
                                                                     self.array_type_objects['dry_cleanings_dyeing']['path']),
                                  'furniture_services': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'furniture_services',
                                                                     self.array_type_objects['furniture_services']['path']),
                                  'hairdressers': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'hairdressers',
                                                                     self.array_type_objects['hairdressers']['path']),
                                  'home_electronics_services': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'home_electronics_services',
                                                                     self.array_type_objects['home_electronics_services']['path']),
                                  'jewelry_services': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'jewelry_services',
                                                                     self.array_type_objects['jewelry_services']['path']),
                                  'laundries': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'laundries',
                                                                     self.array_type_objects['laundries']['path']),
                                  'metal_services': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'metal_services',
                                                                     self.array_type_objects['metal_services']['path']),
                                  'other_domestic_services': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'other_domestic_services',
                                                                     self.array_type_objects['other_domestic_services']['path']),
                                  'pawnshops': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'pawnshops',
                                                                     self.array_type_objects['pawnshops']['path']),
                                  'photo_studios': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'photo_studios',
                                                                     self.array_type_objects['photo_studios']['path']),
                                  'rental_services': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'rental_services',
                                                                     self.array_type_objects['rental_services']['path']),
                                  'ritual_services': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'ritual_services',
                                                                     self.array_type_objects['ritual_services']['path']),
                                  'saunas': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'saunas',
                                                                     self.array_type_objects['saunas']['path']),
                                  'self_service_dry_cleaners': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'self_service_dry_cleaners',
                                                                     self.array_type_objects['self_service_dry_cleaners']['path']),
                                  'self_service_laundries': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'self_service_laundries',
                                                                     self.array_type_objects['self_service_laundries']['path']),
                                  'shoe_services': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'shoe_services',
                                                                     self.array_type_objects['shoe_services']['path']),
                                  'watch_services': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'watch_services',
                                                                     self.array_type_objects['watch_services']['path']),
                                  'data_wifi': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                                              self.low_point_pix,
                                                                                              'data_wifi',
                                                                                              self.array_type_objects[
                                                                                                  'data_wifi'][
                                                                                                  'path']),
                                  'builds': self.get_array_objects_from_file_data_set(self.hi_point_pix,
                                                                     self.low_point_pix,
                                                                     'builds',
                                                                     self.array_type_objects['builds']['path'])
                                  }

    def get_array_objects_from_file_data_set(self, hi_point=[55.7744, 37.580],
                                             low_point=[55.7294, 37.652],
                                             name_array='nonsens',
                                             name_files='lll.csv') -> list:
        array_def = []
        if name_array != 'data_wifi':
            with open(name_files, 'r', encoding='utf-8') as is_f:
                k = 0
                for line in is_f:
                    k += 1
                    ddd = ''
                    analiz = Data_set(line,
                                      self.array_type_objects[name_array]['sep'],
                                      self.hi_point_pix,
                                      self.low_point_pix, name_files)
                    if name_array == 'theaters': ddd = analiz.theatres()

                    if name_array == 'food' and k != 1: ddd = analiz.food()

                    if name_array == 'intercepting_parking': ddd = analiz.intercepting_parking()

                    if name_array == 'paid_parking': ddd = analiz.paid_parking()

                    if name_array == 'closed_paid_parking': ddd = analiz.closed_paid_parking()

                    if name_array == 'cinemas': ddd = analiz.cinemas()

                    if name_array == 'circus': ddd = analiz.circus()

                    if name_array == 'concert_halls': ddd = analiz.concert_halls()

                    if name_array == 'museums': ddd = analiz.museums()

                    if name_array == 'monuments': ddd = analiz.monuments()

                    if name_array == 'education': ddd = analiz.education()

                    if name_array == 'parks': ddd = analiz.parks()

                    if name_array == 'metro_exits': ddd = analiz.metro_exits()

                    if name_array == 'atelier': ddd = analiz.atelier()

                    if name_array == 'bathing_services': ddd = analiz.bathing_services()

                    if name_array == 'comprehensive_domestic_services': ddd = analiz.comprehensive_domestic_services()

                    if name_array == 'dry_cleanings_dyeing': ddd = analiz.dry_cleanings_dyeing()

                    if name_array == 'furniture_services': ddd = analiz.furniture_services()

                    if name_array == 'hairdressers': ddd = analiz.hairdressers()

                    if name_array == 'home_electronics_services': ddd = analiz.home_electronics_services()

                    if name_array == 'jewelry_services': ddd = analiz.jewelry_services()

                    if name_array == 'laundries': ddd = analiz.laundries()

                    if name_array == 'metal_services': ddd = analiz.metal_services()

                    if name_array == 'other_domestic_services': ddd = analiz.other_domestic_services()

                    if name_array == 'pawnshops': ddd = analiz.pawnshops()

                    if name_array == 'photo_studios': ddd = analiz.photo_studios()

                    if name_array == 'rental_services': ddd = analiz.rental_services()

                    if name_array == 'ritual_services': ddd = analiz.ritual_services()

                    if name_array == 'saunas': ddd = analiz.saunas()

                    if name_array == 'self_service_dry_cleaners': ddd = analiz.self_service_dry_cleaners()

                    if name_array == 'self_service_laundries': ddd = analiz.self_service_laundries()

                    if name_array == 'shoe_services': ddd = analiz.shoe_services()

                    if name_array == 'watch_services': ddd = analiz.watch_services()

                    if name_array == 'builds': ddd = analiz.builds()

                    if ddd: array_def.append(ddd)
        if name_array == 'data_wifi':
            analiz = Data_set('line',
                              self.array_type_objects[name_array]['sep'],
                              self.hi_point_pix,
                              self.low_point_pix, name_files)
            ddd = analiz.data_wifi()
            if ddd: array_def.append(ddd)
        return array_def

# test classes

if __name__ == '__main__':
    from servis_modules import get_end_coord_rectangle
    # 55.754311° 37.522732°
    # 55.701605° 37.70619°
    # start_width = 55.7744
    # start_long = 37.580
    # end_width = 55.7294
    # end_long = 37.652
    start_width = 55.754311
    start_long = 37.522732
    end_width = 55.701605
    end_long = 37.70619

    zoom = 12  # start zoom

    # this coordinates center rectangle
    pcc = (start_long + end_long) / 2
    lcc = (start_width + end_width) / 2
    hi_point = [start_width, start_long]
    low_point = [end_width, end_long]
    print('low_point 1 = ', low_point)
    leng_side = 3000
    low_point = get_end_coord_rectangle(hi_point, low_point, leng_side)
    print('low_point 2 = ', low_point)

    param = {'coord_pix': [[pcc, lcc], hi_point, low_point]}
    main_reactange = One_pix(param)
    print(main_reactange)
