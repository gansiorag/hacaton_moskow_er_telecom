import json
from pprint import pprint
from collections import Counter
import pandas as pd

# with open('all_rest.csv','r') as is_f:
#     for line in is_f:
#         pprint(line)
array_key = Counter()
# format_obchepit = 'ID^Name^global_id^IsNetObject^OperatingCompany^TypeObject^AdmArea^\
#          District^Address^PublicPhone^SeatsCount^SocialPrivileges^Longitude_WGS84^\
#          Latitude_WGS84^geoData^geodata_center\n'
format_obchepit = 'ID^Name^global_id^IsNetObject^OperatingCompany^TypeObject^AdmArea^' \
                  'District^Address^SeatsCount^SocialPrivileges^Longitude_WGS84^Latitude_WGS84\n'
f_rez = open('общепит_data-4275-2021-06-01.csv','a')
f_rez.write(format_obchepit)
#with open('/home/al/PycharmProjects/hacaton_moskow_er_telecom/data_set/Выставочные_залы_Москвы_data-7372-2020-12-22.json','r') as is_f:
#with open('/home/al/PycharmProjects/hacaton_moskow_er_telecom/data_set/Музеи_data-7422-2021-05-27.json','r') as is_f:
#with open('/home/al/PycharmProjects/hacaton_moskow_er_telecom/data_set/Театры_data-7432-2021-04-23.json', 'r') as is_f:
with open('/home/al/PycharmProjects/hacaton_moskow_er_telecom/data_set/общепит_data-4275-2021-06-01.json',
              'r') as is_f:
    data = json.load(is_f)
    for ittem in data:
        f_rez.write(f"{ittem['ID']}^"
         f"{ittem['Name']}^"
         f"{ittem['global_id']}^"
         f"{ittem['IsNetObject']}^"
         f"{ittem['OperatingCompany']}^"
         f"{ittem['TypeObject']}^"
         f"{ittem['AdmArea']}^"
         f"{ittem['District']}^"
         f"{ittem['Address']}^"
         #f"{ittem['PublicPhone']}^"
         f"{ittem['SeatsCount']}^"
         f"{ittem['SocialPrivileges']}^"
         f"{ittem['Longitude_WGS84']}^"
         f"{ittem['Latitude_WGS84']}\n")
         #f"{ittem['geoData']}^"
         #f"{ittem['geodata_center']}\n")
    #     for field in ittem:
    #         array_key[field] += 1
    # pprint(array_key)
    # ish_data = pd.read_csv('/home/al/PycharmProjects/hacaton_moskow_er_telecom/общепит_data-4275-2021-06-01.csv',
    #                        sep = '^', header= 0)
    # print(ish_data.head(10))