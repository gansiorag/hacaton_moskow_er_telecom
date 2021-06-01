import json
from pprint import pprint

# with open('all_rest.csv','r') as is_f:
#     for line in is_f:
#         pprint(line)
#with open('/home/al/PycharmProjects/hacaton_moskow_er_telecom/data_set/Выставочные_залы_Москвы_data-7372-2020-12-22.json','r') as is_f:
#with open('/home/al/PycharmProjects/hacaton_moskow_er_telecom/data_set/Музеи_data-7422-2021-05-27.json','r') as is_f:
with open('/home/al/PycharmProjects/hacaton_moskow_er_telecom/data_set/Театры_data-7432-2021-04-23.json', 'r') as is_f:
    data = json.load(is_f)
    pprint(len(data))