import pandas as pd

class Data_set():
    def __init__(self, line, sep, hi_point, low_point, name_files):
        self.hi_point_pix = hi_point
        self.low_point_pix = low_point
        self.servis_list = line.strip().split(sep)
        self.name_files = name_files

    def theatres(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[3].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[3].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                'adress':self.servis_list[1].strip(),
                'ltt': float(self.servis_list[3].strip()),
                'lnt': float(self.servis_list[2].strip())}
        return one_object

    def food(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[1].strip(),
                'net': self.servis_list[3].strip(),
                'type_vid': self.servis_list[5].strip(),
                'adress':self.servis_list[8].strip(),
                'chears':self.servis_list[9].strip(),
                'ltt': float(self.servis_list[-1].strip()),
                'lnt': float(self.servis_list[-2].strip())}
        return one_object

    def builds(self) -> dict:
        one_object = {}
        print(float(self.servis_list[4].strip()))
        if (float(self.servis_list[4].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[4].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[3].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[3].strip()) <= self.low_point_pix[1]) :
            one_object = {
                'type_vid': self.servis_list[0].strip(),
                'adress':self.servis_list[1].strip(),
                'kad_n':self.servis_list[2].strip(),
                'ltt': float(self.servis_list[4].strip()),
                'lnt': float(self.servis_list[3].strip())}
        return one_object

    def intercepting_parking(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                'schedule': self.servis_list[1].strip(),
                'car_capacity': self.servis_list[2].strip(),
                'lnt': float(self.servis_list[3].strip()),
                'ltt': float(self.servis_list[4].strip())}
        return one_object

    def paid_parking(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                'car_capacity': self.servis_list[1].strip(),
                'address': self.servis_list[2].strip(),
                'lnt': float(self.servis_list[3].strip()),
                'ltt': float(self.servis_list[4].strip())}
        return one_object

    def closed_paid_parking(self) -> dict:
        one_object = {}
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                  'schedule': self.servis_list[1].strip(),
                  'car_capacity': self.servis_list[2].strip(),
                  'address': self.servis_list[3].strip(),
                  'lnt': float(self.servis_list[5].strip()),
                  'ltt': float(self.servis_list[4].strip())}
        return one_object

    def cinemas(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                  'address': self.servis_list[1].strip(),
                  'lnt': float(self.servis_list[2].strip()),
                  'ltt': float(self.servis_list[3].strip())}
        return one_object

    def circus(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                  'address': self.servis_list[1].strip(),
                  'lnt': float(self.servis_list[2].strip()),
                  'ltt': float(self.servis_list[3].strip())}
        return one_object

    def concert_halls(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                  'address': self.servis_list[1].strip(),
                  'lnt': float(self.servis_list[2].strip()),
                  'ltt': float(self.servis_list[3].strip())}
        return one_object

    def museums(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                  'address': self.servis_list[1].strip(),
                  'lnt': float(self.servis_list[2].strip()),
                  'ltt': float(self.servis_list[3].strip())}
        return one_object

    def monuments(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                  'address': self.servis_list[1].strip(),
                  'lnt': float(self.servis_list[2].strip()),
                  'ltt': float(self.servis_list[3].strip())}
        return one_object

    def education(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                  'address': self.servis_list[1].strip(),
                  'lnt': float(self.servis_list[2].strip()),
                  'ltt': float(self.servis_list[3].strip())}
        return one_object

    def parks(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                  'address': self.servis_list[1].strip(),
                  'lnt': float(self.servis_list[2].strip()),
                  'ltt': float(self.servis_list[3].strip())}
        return one_object

    def metro_exits(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                  'lnt': float(self.servis_list[1].strip()),
                  'ltt': float(self.servis_list[2].strip())}
        return one_object

    def atelier(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                  'address': self.servis_list[2].strip(),
                  'lnt': float(self.servis_list[3].strip()),
                  'ltt': float(self.servis_list[4].strip())}
        return one_object

    def bathing_services(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def comprehensive_domestic_services(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def dry_cleanings_dyeing(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def furniture_services(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def hairdressers(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def home_electronics_services(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def jewelry_services(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def laundries(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def metal_services(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def other_domestic_services(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def pawnshops(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def photo_studios(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def rental_services(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def ritual_services(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def saunas(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def self_service_dry_cleaners(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def self_service_laundries(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def shoe_services(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def watch_services(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip()) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                          'address': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip()),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def builds(self) -> dict:
        one_object = {}
        #print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[-1].strip()) <= self.hi_point_pix[0] and
        float(self.servis_list[-1].strip()) >= self.low_point_pix[0] and
        float(self.servis_list[-2].strip().replace('[', '')) >= self.hi_point_pix[1] and
        float(self.servis_list[-2].strip().replace('[', '')) <= self.low_point_pix[1]) :
            one_object = {'type': self.servis_list[0].strip(),
                          'address': self.servis_list[1].strip(),
                          'cadastral_number': self.servis_list[2].strip(),
                          'lnt': float(self.servis_list[3].strip().replace('[', '')),
                          'ltt': float(self.servis_list[4].strip())}
        return one_object

    def data_wifi(self) -> dict:
        one_object = {'nabor':[],
                                    'kol_point_wifi':0.0,
                                    'kol_devices':0.0,
                                    'kol_events':0.0,
                                    'activity_people':0.0}
        servis_list_event = []
        servis_list_camers = []
        servis_list_device = []
        #print(float(self.servis_list[2].strip()))
        data_day_20 = pd.read_csv(self.name_files, header = 0, sep = '^')
        servis_data = data_day_20.loc[(data_day_20['ltt'].astype(float) <= self.hi_point_pix[0]) &
                                      (data_day_20['ltt'].astype(float) >= self.low_point_pix[0]) &
                                      (data_day_20['lnt'].astype(float) >= self.hi_point_pix[1]) &
                                      (data_day_20['lnt'].astype(float) <= self.low_point_pix[1])]
        one_object['nabor'] = servis_data
        one_object['kol_point_wifi'] = len(servis_data['ap_mac'].unique())
        one_object['kol_devices'] = len(servis_data['device_id'].unique())
        one_object['kol_events'] =len(servis_data['ltt'])
        if (one_object['kol_point_wifi']>0 and
            one_object['kol_devices']>0) :
                one_object['activity_people'] = round(one_object['kol_events']/
                                                                (one_object['kol_point_wifi']*
                                                                 one_object['kol_devices']), 3)
        print(one_object['kol_point_wifi'])
        print(one_object['kol_devices'])
        print(one_object['kol_events'])
        print(one_object['activity_people'])
        return one_object



