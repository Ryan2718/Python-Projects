# -*- coding: utf-8 -*-

class ClimateData(object):
    def __init__(self, monthly_avg_tmps, monthly_avg_precips, hemisphere):
        self.monthly_avg_tmps    = monthly_avg_tmps # Degree C
        self.monthly_avg_precips = monthly_avg_precips # mm
        self.hemisphere         = hemisphere
