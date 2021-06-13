from flask import Flask

session = {'user':{'legal_data':{},
                   'name':'',
                   'adress':'',
                   'base_activity':'food',
                   'fin_data':{},
                   'coordinates':[],
                   'special_data':{}},
           'type_obj':['atelier','bathing_services', 'builts', 'cinemas', 'circus', 'closed_paid_parking',
                        'comprehensive_domestic_services', 'concert_halls', 'data_wifi', 'dry_cleanings_dyeing',
                        'education', 'food', 'furniture_services', 'hairdressers', 'home_electronics_services',
                        'intercepting_parking', 'jewelry_services', 'laundries', 'metal_services', 'metro_exits',
                        'museums', 'other_domestic_services', 'paid_parking', 'parks', 'pawnshops','photo_studios',
                        'rental_services', 'ritual_services', 'saunas', 'self_service_dry_cleaners',
                        'self_service_laundries', 'shoe_services', 'theaters', 'watch_services']
           }

app = Flask(__name__)

