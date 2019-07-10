# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '../data')
import data.data_climate as dc
import climate.koppen_classifier as kc

def test_koppen():
    assert kc.classify(dc.san_francisco) == 'Csb'
