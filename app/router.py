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
    leng_side = 1000
    kol_sqrt_width, kol_sqrt_long, koef_lend, array_sqrt = get_array_borders_squere(hi_point = [55.7744, 37.580],
                                                                                    low_point = [55.7294, 37.652],
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




