import random as rd
import numpy as np

def create_array2d(rows, columns):
    array = []
    for i in range(rows):
        row = []
        for j in range(columns):
            value = rd.randint(1,10)
            row.append(value)
        array.append(row)
    return array

num_rows = int(input("input row: "))
num_columns = int(input("input column: "))

my_array2d = create_array2d(num_rows, num_columns)


def sum_array(my_array2d):
    tong = 0
    for hang in my_array2d:
        for so in hang:
            tong += so
    return tong

tong_cac_so = sum_array(my_array2d)


for row in my_array2d:
    print(row)


print(tong_cac_so)

def sum_row(my_array2d,columns):
    tong = 0
    tong = sum(my_array2d[columns])
    return tong

tong_so = sum_row(my_array2d,num_columns)
print(tong_so)


