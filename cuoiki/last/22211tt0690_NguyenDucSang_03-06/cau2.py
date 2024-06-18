# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:53:15 2024

@author: Administrator
"""

import pandas as pd
import numpy as np

df_od = pd.read_csv("Online_Retail.csv",encoding="latin1")

# Câu A:
print("5 dòng đầu tiên")
print(df_od.head(5))
print()
print("a các kiểu dữ liệu của các field")
print(df_od.dtypes)
print()
print("Lây dữ liệu 10 dòng  StockCode, Description, Quantity,InvoiceDate, UnitPrice")
print(df_od.loc[:10],['StockCode', 'Description', 'Quantity','InvoiceDate', 'UnitPrice'])
print()
print("Lấy ra các dòng từ [10:20] của các trường StockCode, Quantity,InvoiceDate, UnitPrice, CustomerID, Country")
print(df_od.loc[10:20],['StockCode', 'Description', 'Quantity','InvoiceDate', 'UnitPrice'])
print()

#Câu B:
print("Thống kê các hoá đơn (Invoice No) theo từng vùng(Country)")
print(df_od.groupby('Country')['InvoiceNo'].nunique())
print()
print("Lấy ra 10 hoá đơn có đơn giá (UnitPrice) cao nhất")
print(df_od.nlargest(10, 'UnitPrice'))
print("Lấy ra 5 khách hàng ở United KingDom mà mua hàng có đơn giá cao nhất")
print(df_od.nlargest(5, 'UnitPrice'))
print()
print("Tạo bảng thống kê (min, max, avg, mean, median) của các số lượng (Quantity) theo từng quốc gia (Country)")
print(df_od.groupby('Country')['Quantity'].agg(['min', 'max', 'mean', 'median']))
