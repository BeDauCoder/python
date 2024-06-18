# -*- coding: utf-8 -*-
"""
Created on Sun May 28 07:29:36 2023

@author: WINDOWS
"""

class SinhVien:
 
    def __init__(self, id, name, sex, age, diemToan, diemLy, diemHoa):
        self._id = id
        self._name = name
        self._sex = sex
        self._age = age
        self._diemToan = diemToan
        self._diemLy = diemLy
        self._diemHoa = diemHoa
        self._diemTB = 0
        self._hocLuc = ""