"""
This module make

Author Gansior A. mail - gansior@gansior.ru tel - +79173383804
"""
from app import app
from flask import render_template
from app.servis_modules import get_array_borders_squere


@app.route("/mapss")
def map():
    pcc = 37.620000
    lcc = 55.752900
    zoom = 12
    level = 100
    start_width = 55.7744
    start_long = 37.580
    end_width = 55.7294
    end_long = 37.652
    leng_side = 500
    kol_sqrt_width, kol_sqrt_long, koef_lend, array_sqrt = get_array_borders_squere(hi_point = [start_width, start_long],
                                                                                    low_point = [end_width, end_long],
                                                                                    leng_side = leng_side)

    return render_template('map_index.html',
                            lcc = lcc,
                            pcc = pcc,
                            zoom = zoom,
                            level = level,
                            start_width = start_width,
                            start_long = start_long,
                            end_width = end_width,
                            end_long = end_long,
                            leng_side = leng_side,
                            kol_sqrt_width = kol_sqrt_width,
                            kol_sqrt_long = kol_sqrt_long,
                            koef_lend = koef_lend
                            )

@app.route("/")
def index():
    title = "Первая страница"
    return render_template('/index.html', title = title)

@app.route("/coord")
def coord():
    title = "Кординаты"
    return render_template('/coord.html', title = title)

@app.route("/hist")
def hist():
    title = "hist"
    return render_template('/hist.html', title = title)

@app.route("/optimisetion_potr")
def optimisetion_potr():
    title = "optimisetion_potr"
    return render_template('/optimisetion_potr.html', title = title)

@app.route("/coords_by_address")
def coords_by_address():
    title = "coords_by_address"
    return render_template('/coords_by_address.html', title = title)

@app.route("/valuation_by_coords")
def valuation_by_coords():
    title = "valuation_by_coords"
    return render_template('/valuation_by_coords.html', title = title)

@app.route("/search_by_heat_map")
def search_by_heat_map():
    title = "search_by_heat_map"
    return render_template('/search_by_heat_map.html', title = title)

@app.route("/valuation_by_distance")
def valuation_by_distance():
    title = "valuation_by_distance"
    return render_template('/valuation_by_distance.html', title = title)

@app.route("/valuation_by_district")
def valuation_by_district():
    title = "valuation_by_district"
    return render_template('/valuation_by_district.html', title = title)

@app.route("/setting_signal_points")
def setting_signal_points():
    title = "setting_signal_points"
    return render_template('/setting_signal_points.html', title = title)

@app.route("/buisness_state_at_the_moment")
def buisness_state_at_the_moment():
    title = "buisness_state_at_the_moment"
    return render_template('/buisness_state_at_the_moment.html', title = title)

@app.route("/buisness_state_and_rivalry")
def buisness_state_and_rivalry():
    title = "buisness_state_and_rivalry"
    return render_template('/buisness_state_and_rivalry.html', title = title)

@app.route("/choose_model")
def choose_model():
    title = "choose_model"
    return render_template('/choose_model.html', title = title)

@app.route("/admin")
def admin():
    title = "admin"
    return render_template('/admin.html', title = title)

@app.route("/reference_book")
def reference_book():
    title = "reference_book"
    return render_template('/reference_book.html', title = title)

@app.route("/support")
def support():
    title = "support"
    return render_template('/support.html', title = title)

@app.route("/info")
def info():
    title = "info"
    return render_template('/info.html', title = title)

@app.route("/contacts")
def contacts():
    title = "contacts"
    return render_template('/contacts.html', title = title)
