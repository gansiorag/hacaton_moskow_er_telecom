from flask import Flask

session = {'user':{'legal_data':{},
                   'fin_data':{},
                   'special_data':{}}
           }

app = Flask(__name__)

