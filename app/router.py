"""
This module make

Author Gansior A. mail - gansior@gansior.ru tel - +79173383804
"""
from flask import render_template
from flask import request
from app import app
from app.servis_modules import get_array_borders_squere, get_end_coord_rectangle
from app.class_Onix import One_pix
from app.servis_modules import Work_with_One_pix
from app import session
import random
import copy
from numpy import mean

@app.route("/")
def index():
    title = "Первая страница"
    return render_template('/index.html', title=title)


@app.route("/legal_data", methods=['GET', 'POST'])
def coord():
    title = "Юридические данные"
    session['user']['name'] = request.values.get('USER_NAME')
    session['user']['adress'] = request.values.get('USER_ADRESS')
    session['user']['legal_data']['all_activities'] = request.values.get('ALL_ACTIVITIES')
    session['user']['legal_data']['dislocation_address'] = request.values.get('DISLOCATION_ADDRESS')
    session['user']['legal_data']['inn'] = request.values.get('INN')
    session['user']['legal_data']['orgn'] = request.values.get('OGRN')
    session['user']['legal_data']['activity'] = request.values.get('ACTIVITY')
    session['user']['legal_data']['boss'] = request.values.get('BOSS')
    session['user']['legal_data']['sex'] = request.values.get('SEX')
    session['user']['legal_data']['age'] = request.values.get('AGE')
    session['user']['legal_data']['education'] = request.values.get('EDUCATION')
    session['user']['legal_data']['authorized_capital'] = request.values.get('AUTHORIZED_CAPITAL')
    print(session['user']['name'], session['user']['adress'], print(session['user']['legal_data']))
    return render_template('/legal_data.html', title=title)


@app.route("/fin_data")
def fin_data():
    title = "Финансовые данные"
    session['user']['fin_data']['employees'] = request.values.get('EMPLOYEES')
    session['user']['fin_data']['affiliate'] = request.values.get('AFFILIATE')
    session['user']['fin_data']['records_from_tax_office'] = request.values.get('RECORDS_FROM_TAX_OFFICE')
    session['user']['fin_data']['fair_business_data'] = request.values.get('FAIR_BUSINESS_DATA')
    print(session['user']['fin_data'])
    return render_template('/fin_data.html', title=title)


@app.route("/special_data")
def hist():
    title = "Специальные даные"
    return render_template('/special_data.html', title=title)


@app.route("/valuation_by_address",methods=['GET', 'POST'])
def valuation_by_address():
    list_obj = []
    if request.method == 'POST':
        list_obj = request.form.getlist('type_obj')
        print(list_obj)

        if len(list_obj) > 0:
            for objj in session['type_obj']:
                if objj in list_obj:
                    session['type_obj'][objj][1] = 'checked'
                else:
                    session['type_obj'][objj][1] = ''
        else:
            for objj in session['type_obj']: session['type_obj'][objj][1] = ''

    start_width = 55.754311
    start_long = 37.522732
    end_width = 55.701605
    end_long = 37.70619
    hi_point = [start_width, start_long]
    low_point = [end_width, end_long]
    leng_side = 1250
    low_point = get_end_coord_rectangle(hi_point, low_point, leng_side)
    zoom = 11  # start zoom

    # this coordinates center rectangle
    pcc = (start_long + low_point[1]) / 2
    lcc = (start_width + low_point[0]) / 2

    param = {'coord_pix': [[pcc, lcc], hi_point, low_point]}
    main_reactange = One_pix(param)
    kol_sqrt_width, kol_sqrt_long, koef_lend, array_sqrt = get_array_borders_squere(hi_point=[start_width, start_long],
                                                                                    low_point=[end_width, end_long],
                                                                                    leng_side=leng_side)
    print('kol_sqrt_width, kol_sqrt_long = ', kol_sqrt_width, kol_sqrt_long)
    work_array = Work_with_One_pix(main_reactange.array_objects_pix)
    print(list_obj)
    rezult = work_array.divide_data_sqrt(array_sqrt, list_obj)
    print(rezult)

    address = request.values.get('ADDRESS')

    return render_template('valuation_by_address.html',
                           lcc=lcc,
                           pcc=pcc,
                           zoom=zoom,
                           start_width=start_width,
                           start_long=start_long,
                           end_width=low_point[0],
                           end_long=low_point[1],
                           leng_side=leng_side,
                           kol_sqrt_width=kol_sqrt_width,
                           kol_sqrt_long=kol_sqrt_long,
                           koef_lend=koef_lend,
                           names_obj=session['type_obj'],
                           see_obj=rezult
                           )

@app.route("/valuation_by_coords",methods=['GET', 'POST'])
def valuation_by_coords():
    list_obj = []
    if request.method == 'POST':
        list_obj = request.form.getlist('type_obj')
        print(list_obj)

        if len(list_obj) > 0:
            for objj in session['type_obj']:
                if objj in list_obj:
                    session['type_obj'][objj][1] = 'checked'
                else:
                    session['type_obj'][objj][1] = ''
        else:
            for objj in session['type_obj']: session['type_obj'][objj][1] = ''

    start_width = 55.754311
    start_long = 37.522732
    end_width = 55.701605
    end_long = 37.70619
    hi_point = [start_width, start_long]
    low_point = [end_width, end_long]
    leng_side = 1250
    low_point = get_end_coord_rectangle(hi_point, low_point, leng_side)
    zoom = 11  # start zoom

    # this coordinates center rectangle
    pcc = (start_long + low_point[1]) / 2
    lcc = (start_width + low_point[0]) / 2

    param = {'coord_pix': [[pcc, lcc], hi_point, low_point]}
    main_reactange = One_pix(param)
    kol_sqrt_width, kol_sqrt_long, koef_lend, array_sqrt = get_array_borders_squere(hi_point=[start_width, start_long],
                                                                                    low_point=[end_width, end_long],
                                                                                    leng_side=leng_side)
    print('kol_sqrt_width, kol_sqrt_long = ', kol_sqrt_width, kol_sqrt_long)
    work_array = Work_with_One_pix(main_reactange.array_objects_pix)
    print(list_obj)
    rezult = work_array.divide_data_sqrt(array_sqrt, list_obj)
    print(rezult)

    coords = request.values.get('COORDS')

    return render_template('valuation_by_coords.html',
                           lcc=lcc,
                           pcc=pcc,
                           zoom=zoom,
                           start_width=start_width,
                           start_long=start_long,
                           end_width=low_point[0],
                           end_long=low_point[1],
                           leng_side=leng_side,
                           kol_sqrt_width=kol_sqrt_width,
                           kol_sqrt_long=kol_sqrt_long,
                           koef_lend=koef_lend,
                           names_obj=session['type_obj'],
                           see_obj=rezult
                           )

@app.route("/search_by_heat_map",methods=['GET', 'POST'])
def search_by_heat_map():
    '''
     parameters for starts page
    this parameters base reсtangle jn map - coordinates highe of left angle and low of rigth angle
    координаты садового кольца
    start_width = 55.7744
    start_long = 37.580
    end_width = 55.7294
    end_long = 37.652

    :return:
    '''

    list_obj = []
    if request.method == 'POST':
        list_obj = request.form.getlist('type_obj')
        print(list_obj)

        if len(list_obj) > 0:
            for objj in session['type_obj']:
                if objj in list_obj:
                    session['type_obj'][objj][1] = 'checked'
                else:
                    session['type_obj'][objj][1] = ''
        else:
            for objj in session['type_obj']: session['type_obj'][objj][1] = ''

    start_width = 55.754311
    start_long = 37.522732
    end_width = 55.701605
    end_long = 37.70619
    hi_point = [start_width, start_long]
    low_point = [end_width, end_long]
    leng_side = 1250
    low_point = get_end_coord_rectangle(hi_point, low_point, leng_side)
    zoom = 11  # start zoom

    # this coordinates center rectangle
    pcc = (start_long + low_point[1]) / 2
    lcc = (start_width + low_point[0]) / 2

    param = {'coord_pix': [[pcc, lcc], hi_point, low_point]}
    main_reactange = One_pix(param)
    kol_sqrt_width, kol_sqrt_long, koef_lend, array_sqrt = get_array_borders_squere(hi_point=[start_width, start_long],
                                                                                    low_point=[end_width, end_long],
                                                                                    leng_side=leng_side)
    print('kol_sqrt_width, kol_sqrt_long = ', kol_sqrt_width, kol_sqrt_long)
    work_array = Work_with_One_pix(main_reactange.array_objects_pix)
    print(list_obj)
    rezult = work_array.divide_data_sqrt(array_sqrt, list_obj)
    # new_rez = []
    # if len(list_obj) < len(rezult[0]):
    #    for dd in rezult:
    #
    # else: new_rez = copy.deepcopy(rezult)
    # print(new_rez)
    return render_template('search_by_heat_map.html',
                           lcc=lcc,
                           pcc=pcc,
                           zoom=zoom,
                           start_width=start_width,
                           start_long=start_long,
                           end_width=low_point[0],
                           end_long=low_point[1],
                           leng_side=leng_side,
                           kol_sqrt_width=kol_sqrt_width,
                           kol_sqrt_long=kol_sqrt_long,
                           koef_lend=koef_lend,
                           names_obj = session['type_obj'],
                           see_obj = rezult
                           )


@app.route("/valuation_by_distance")
def valuation_by_distance():
    title = "valuation_by_distance"
    return render_template('/valuation_by_distance.html', title=title)


@app.route("/valuation_by_district")
def valuation_by_district():
    title = "valuation_by_district"
    return render_template('/valuation_by_district.html', title=title)


@app.route("/setting_signal_points")
def setting_signal_points():
    title = "Установка сигнальных точек"
    return render_template('/setting_signal_points.html', title=title)


@app.route("/buisness_state_at_the_moment")
def buisness_state_at_the_moment():
    title = "Состояние бизнеса на текущий момент"
    data_user_first = [{'date': list(range(1, 31)), 'data': [random.randint(1, 12041) for i in range(0, 31)],
                        'data_max_power': [random.randint(1, 9582) for i in range(0, 31)],
                        'data_qv75': [random.randint(1, 8300) for i in range(0, 31)]}]
    data_user_second = [{'date': list(range(1, 31)), 'data': [random.randint(1, 3452) for i in range(0, 31)],
                         'data_max_power': [random.randint(1, 4631) for i in range(0, 31)],
                         'data_qv75': [random.randint(1, 12041) for i in range(0, 31)]}]
    first_mass = ["Дата", "Около вашей точки", "Популярность вашей точки", "Активность возле вашей точки"]
    second_mass = ["Дата", "15 мин.", "30 мин.", "1 час"]
    graf_title_first = 'График пешеходного трафика по часам'
    graf_title_second = 'Кол-во потенциальных клиентов возле точки'
    return render_template('/buisness_state_at_the_moment.html', title=title, data_user_first=data_user_first,
                           data_user_second=data_user_second, first_mass=first_mass, second_mass=second_mass,
                           graf_title_first=graf_title_first, graf_title_second=graf_title_second,
                           avg_params_first=[int(mean(data_user_first[0]['data'])), int(mean(data_user_first[0]['data_max_power'])), int(mean(data_user_first[0]['data_qv75']))], avg_params_second=[int(mean(data_user_second[0]['data'])), int(mean(data_user_second[0]['data_max_power'])), int(mean(data_user_second[0]['data_qv75']))])


@app.route("/buisness_state_and_rivalry")
def buisness_state_and_rivalry():
    title = "Состояние бизнеса и конкуренты"
    data_user_first = [{'date': list(range(1, 31)), 'data': [random.randint(1, 12041) for i in range(0, 31)],
                        'data_max_power': [random.randint(1, 9582) for i in range(0, 31)],
                        'data_qv75': [random.randint(1, 8300) for i in range(0, 31)]}]
    data_user_second = [{'date': list(range(1, 31)), 'data': [random.randint(1, 3452) for i in range(0, 31)],
                         'data_max_power': [random.randint(1, 4631) for i in range(0, 31)],
                         'data_qv75': [random.randint(1, 7942) for i in range(0, 31)]}]
    first_mass = ["Дата", "Около вашей точки", "Ср. трафик около точек конкурентов", "Общий трафик по квадрату"]
    second_mass = ["Дата", "Популярность вашей точки", "Средняя популярность точки у конкурентов", "Поплуярность квадрата"]
    graf_title_first = 'График пешеходного трафика по часам'
    graf_title_second = 'График изменения популярности места по часам'
    return render_template('/buisness_state_and_rivalry.html', title=title, data_user_first=data_user_first,
                           data_user_second=data_user_second, first_mass=first_mass, second_mass=second_mass,
                           graf_title_first=graf_title_first, graf_title_second=graf_title_second,
                           avg_params_first=[int(mean(data_user_first[0]['data'])), int(mean(data_user_first[0]['data_max_power'])), int(mean(data_user_first[0]['data_qv75']))], avg_params_second=[int(mean(data_user_second[0]['data'])), int(mean(data_user_second[0]['data_max_power'])), int(mean(data_user_second[0]['data_qv75']))])


@app.route("/choose_model")
def choose_model():
    title = "Выбор параметров и моделей обработки и анализа данных."
    return render_template('/choose_model.html', title=title)


@app.route("/admin")
def admin():
    title = "admin"
    return render_template('/admin.html', title=title)


@app.route("/reference_book")
def reference_book():
    title = "reference_book"
    return render_template('/reference_book.html', title=title)


@app.route("/support")
def support():
    title = "support"
    return render_template('/support.html', title=title)


@app.route("/info")
def info():
    title = "info"
    return render_template('/info.html', title=title)


@app.route("/contacts")
def contacts():
    title = "contacts"
    return render_template('/contacts.html', title=title)
