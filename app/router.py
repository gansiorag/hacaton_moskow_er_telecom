"""
This module make

Author Gansior A. mail - gansior@gansior.ru tel - +79173383804
"""
from flask import render_template
from flask import request
from app import app
from app.servis_modules import get_array_borders_squere, get_end_coord_rectangle
from app.servis_modules import One_pix
from app.servis_modules import Work_with_One_pix
from app import session

@app.route("/")
def index():
    title = "Первая страница"
    return render_template('/index.html', title=title)


@app.route("/legal_data", methods=['GET', 'POST'])
def coord():
    title = "Юридические данные"
    session['user']['name'] = request.values.get('USER_NAME')  # Your form's
    session['user']['adress'] = request.values.get('USER_ADRESS') # input names
    print(session['user']['name'], session['user']['adress'])
    return render_template('/legal_data.html', title=title)


@app.route("/fin_data")
def fin_data():
    title = "Финансовые данные"
    return render_template('/fin_data.html', title=title)


@app.route("/special_data")
def hist():
    title = "Специальные даные"
    return render_template('/special_data.html', title=title)


@app.route("/valuation_by_address")
def valuation_by_address():
    title = "valuation_by_address"
    return render_template('/valuation_by_address.html', title=title)


@app.route("/valuation_by_coords")
def valuation_by_coords():
    title = "valuation_by_coords"
    return render_template('/valuation_by_coords.html', title=title)


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
    title = "buisness_state_at_the_moment"
    return render_template('/buisness_state_at_the_moment.html', title=title)


@app.route("/buisness_state_and_rivalry")
def buisness_state_and_rivalry():
    title = "buisness_state_and_rivalry"
    return render_template('/buisness_state_and_rivalry.html', title=title)


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
