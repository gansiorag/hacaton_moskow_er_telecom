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


@app.route("/valuation_by_address")
def valuation_by_address():
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
    name_obj = ['theaters', 'food', 'intercepting_parking', 'paid_parking', 'closed_paid_parking',
                'cinemas', 'circus', 'concert_halls', 'museums', 'education']
    main_reactange = One_pix(param)
    kol_sqrt_width, kol_sqrt_long, koef_lend, array_sqrt = get_array_borders_squere(hi_point=[start_width, start_long],
                                                                                    low_point=[end_width, end_long],
                                                                                    leng_side=leng_side)
    print('kol_sqrt_width, kol_sqrt_long = ', kol_sqrt_width, kol_sqrt_long)
    work_array = Work_with_One_pix(main_reactange.array_objects_pix)

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
                           koef_lend=koef_lend
                           )

@app.route("/valuation_by_coords")
def valuation_by_coords():
    start_width = 55.754311
    start_long = 37.522732
    end_width = 55.701605
    end_long = 37.70619
    hi_point = [start_width, start_long]
    low_point = [end_width, end_long]
    leng_side = 1250
    low_point = get_end_coord_rectangle(hi_point, low_point, leng_side)
    zoom = 11 # start zoom

    # this coordinates center rectangle
    pcc = (start_long + low_point[1]) / 2
    lcc = (start_width + low_point[0]) / 2

    param = {'coord_pix': [[pcc, lcc], hi_point, low_point]}
    name_obj = ['theaters', 'food', 'intercepting_parking', 'paid_parking', 'closed_paid_parking',
                'cinemas', 'circus', 'concert_halls', 'museums', 'education']
    main_reactange = One_pix(param)
    kol_sqrt_width, kol_sqrt_long, koef_lend, array_sqrt = get_array_borders_squere(hi_point=[start_width, start_long],
                                                                                    low_point=[end_width, end_long],
                                                                                    leng_side=leng_side)
    print('kol_sqrt_width, kol_sqrt_long = ', kol_sqrt_width, kol_sqrt_long)
    work_array = Work_with_One_pix(main_reactange.array_objects_pix)

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
                           koef_lend=koef_lend
                           )

@app.route("/search_by_heat_map")
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
    name_obj = ['theaters', 'food', 'intercepting_parking', 'paid_parking', 'closed_paid_parking',
                'cinemas', 'circus', 'concert_halls', 'museums', 'education']
    main_reactange = One_pix(param)
    kol_sqrt_width, kol_sqrt_long, koef_lend, array_sqrt = get_array_borders_squere(hi_point=[start_width, start_long],
                                                                                    low_point=[end_width, end_long],
                                                                                    leng_side=leng_side)
    print('kol_sqrt_width, kol_sqrt_long = ', kol_sqrt_width, kol_sqrt_long)
    work_array = Work_with_One_pix(main_reactange.array_objects_pix)

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
                           koef_lend=koef_lend
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
    data_user = [{'date': list(range(1, 31)), 'data': [random.randint(1, 30) for i in range(1, 31)],
                  'data_max_power': [random.randint(1, 30) for i in range(1, 31)],
                  'data_qv75': [random.randint(1, 30) for i in range(1, 31)]}]
    print(data_user)
    return render_template('/buisness_state_at_the_moment.html', title=title, data_user=data_user)


@app.route("/buisness_state_and_rivalry")
def buisness_state_and_rivalry():
    title = "Состояние бизнеса и конкуренты"
    data_user = [{'date': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'data': [5, 2, 3, 4, 3, 6, 7, 8, 9, 10],
                  'data_max_power': [1, 2, 2, 4, 5, 6, 5, 30, 9, 10], 'data_qv75': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}]
    return render_template('/buisness_state_and_rivalry.html', title=title, data_user=data_user)


@app.route("/choose_model")
def choose_model():
    title = "choose_model"
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
