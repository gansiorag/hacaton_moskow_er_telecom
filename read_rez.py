import json
from pprint import pprint
from collections import Counter

# with open('all_rest.csv','r') as is_f:
#     for line in is_f:
#         pprint(line)
array_key = Counter()
format_obchepit = 'ID^Name^global_id^IsNetObject^OperatingCompany^TypeObject^AdmArea^\
         District^Address^PublicPhone^SeatsCount^SocialPrivileges^Longitude_WGS84^\
         Latitude_WGS84^geoData^geodata_center\n'
f_rez = open('общепит_data-4275-2021-06-01.csv','a')
f_rez.write(format_obchepit)
#with open('/home/al/PycharmProjects/hacaton_moskow_er_telecom/data_set/Выставочные_залы_Москвы_data-7372-2020-12-22.json','r') as is_f:
#with open('/home/al/PycharmProjects/hacaton_moskow_er_telecom/data_set/Музеи_data-7422-2021-05-27.json','r') as is_f:
#with open('/home/al/PycharmProjects/hacaton_moskow_er_telecom/data_set/Театры_data-7432-2021-04-23.json', 'r') as is_f:
with open('/home/al/PycharmProjects/hacaton_moskow_er_telecom/data_set/общепит_data-4275-2021-06-01.json',
              'r') as is_f:
    data = json.load(is_f)
    for ittem in data:
        f_rez.write(f"{ittem['ID'}^"
         f"{ittem['Name': 17298,
         f"{ittem['global_id': 17298,
         f"{ittem['IsNetObject': 17298,
         f"{ittem['OperatingCompany': 17298,
         f"{ittem['TypeObject': 17298,
         f"{ittem['AdmArea': 17298,
         f"{ittem['District': 17298,
         f"{ittem['Address': 17298,
         {ittem['PublicPhone': 17298,
         {ittem['SeatsCount': 17298,
         {ittem['SocialPrivileges': 17298,
         {ittem['Longitude_WGS84': 17298,
         {ittem['Latitude_WGS84': 17298,
         {ittem['geoData': 17298,
         {ittem['geodata_center': 17298})}")
        for field in ittem:
            array_key[field] += 1
    pprint(array_key)