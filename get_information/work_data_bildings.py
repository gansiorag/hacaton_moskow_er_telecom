import json
"""
This module make

Author Gansior A. mail - gansior@gansior.ru tel - +79173383804
"""
import json

# def proga():
#     data_is = json.loads('/home/al/PycharmProjects/hacaton_moskow_er_telecom/app/data_set/здания_москвы_data-29580-2021-06-12.json')
#     for build in data_is:


if __name__ == '__main__':
    name_file = '/home/al/PycharmProjects/hacaton_moskow_er_telecom/app/data_set/output_file.json'
    read_file = open(name_file, "r")
    data = read_file.read().split('AID')
    print(len(data))
    rez_file = open('/home/al/PycharmProjects/hacaton_moskow_er_telecom/app/data_set/builds.csv', 'w')
    kol = 0
    for line in data:
        kol += 1
        print(kol)
        type_obj = ''
        adress_obj = ''
        kad_n = ''
        lnt = ''
        ltt = ''
        if '"geoData":{"coordinates":[[[' in line:
            lnt = line.split('"geoData":{"coordinates":[[[')[1].split(',')[0]
            ltt = line.split('"geoData":{"coordinates":[[[')[1].split(',')[1].split('],[')[0]
            if '"OBJ_TYPE":"' in line :
                type_obj = line.split('"OBJ_TYPE":"')[1].split('","')[0]
            if '"ADDRESS":"' in line:
                adress_obj = line.split('"ADDRESS":"')[1].split('","')[0]
            if '"KAD_N":[{"KAD_N":"' in line:
                kad_n = line.split('"KAD_N":[{"KAD_N":"')[1].split('"}],')[0]
            rez_file.write(type_obj + '^' + adress_obj + '^' + kad_n + '^' + lnt + '^' + ltt + '\n')

        # print(type_obj, adress_obj, kad_n, lnt, ltt)
    rez_file.close()