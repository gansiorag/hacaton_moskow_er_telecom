from flask import Flask

session = {'user':{'legal_data':{},
                   'name':'',
                   'adress':'',
                   'fin_data':{},
                   'coordinates':[],
                   'special_data':{}}
           }

app = Flask(__name__)

