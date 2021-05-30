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
    zoom = 5
    level = 100
    return render_template('/map_index.html',lcc = lcc, pcc = pcc, zoom = 13, level = level )

@app.route("/")
def index():
    title = "Первая страница"
    return render_template('/index.html', title = title)




