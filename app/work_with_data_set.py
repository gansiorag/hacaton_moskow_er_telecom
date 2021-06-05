class Data_set():
    def __init__(self, line, sep, hi_point, low_point):
        self.hi_point_pix = hi_point
        self.low_point_pix = low_point
        self.servis_list = line.strip().split(sep)
    
    def theatres(self) -> dict:
        one_object = {}
        print(float(self.servis_list[2].strip()))
        if (float(self.servis_list[3].strip()) <= self.hi_point_pix[0] and 
        float(self.servis_list[3].strip()) >= self.low_point_pix[0] and 
        float(self.servis_list[2].strip()) >= self.hi_point_pix[1] and 
        float(self.servis_list[2].strip()) <= self.low_point_pix[1]) :
            one_object = {'name': self.servis_list[0].strip(),
                'adress':self.servis_list[1].strip(),
                'ltt': float(self.servis_list[3].strip()),
                'lnt': float(self.servis_list[2].strip())}
        return one_object
    