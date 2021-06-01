"""
This module make

Author Gansior A. mail - gansior@gansior.ru tel - +79173383804
"""
from app import app
from flask import render_template

@app.route("/map")
def map():
    pcc = 37.620000
    lcc = 55.752900
    zoom = 13
    level = 100
    start_width = 55.7744
    start_long = 37.580
    end_width = 55.7294
    end_long = 37.66
    leng_side = 100

    # def get_array_borders_squere(hi_point=[55.7744, 37.580], low_point=[55.7294, 37.66], leng_side=100):
    #     width = abs(hi_point[0] - low_point[0])
    #     long = abs(hi_point[1] - low_point[1])
    #     print(width)
    #     print(long)
    #     kol_sqrt = int(width / 0.001)
    #     koef_lend = leng_side / 100.0
    #     print(kol_sqrt)

    return render_template('/map_index.html',lcc = lcc, pcc = pcc, zoom = zoom, level = level,
                            start_width = start_width,
                            start_long = start_long,
                            end_width = end_width,
                            end_long = end_long,
                            leng_side = leng_side
                            )

@app.route("/")
def index():
    title = "Первая страница"
    return render_template('/index.html', title = title)




