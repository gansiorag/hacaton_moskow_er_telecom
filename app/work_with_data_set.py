class Data_set():
    def __init__(self, line, sep, hi_point, low_point):
        self.hi_point_pix = hi_point
        self.low_point_pix = low_point
        self.servis_list = line.strip().split(sep)

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

