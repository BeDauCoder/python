# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
# Một trường đại học quản lý các phòng học, mỗi phòng học đều có mã phòng, dãy nhà,
# diện tích, số bóng đèn. Trong đó, có các loại phòng: phòng học lý thuyết, phòng máy tính.

#Câu 1:

class PhongHoc:
    def __init__(self,maPhong,dayNha,dienTich,soBongDen):
        self.maPhong = maPhong
        self.dayNha = dayNha
        self.dienTich = dienTich
        self.soBongDen = soBongDen
        
        
#Hàm thêm một phòng mới
def addRoom(listRoom):
    # for room in listRoom:
        maPhong = input("Nhập mã phòng: ")
        # if maPhong == room.maPhong:

        dayNha = input("Nhập dãy nhà: ")
        dienTich = float(input("Diện Tích: "))
        soBongDen = int(input("Nhập số bóng đèn: "))
        room = PhongHoc(maPhong, dayNha, dienTich, soBongDen)
        listRoom.append(room)
        # else:
        #     print("Trùng mã")
   
#Hàm xóa phòng
def updateRoom(listRoom):
    maPhong_update = input("Nhập mã phòng cần xửa: ")
    found = False
    for room in listRoom:
        if room.maPhong == maPhong_update:
            found = True
            dayNha_new = input("Nhập dãy nhà mới: ")
            dienTich_new = float(input("Diện Tích mới: "))
            soBongDen_new = int(input("Nhập số bóng đèn: "))
            
            dayNha_new = room.dayNha
            dienTich_new = room.dienTich
            soBongDen_new = room.soBongDen
        if not found:
            print("Không tìm thấy mã phòng")   

   
#Hàm xóa phòng
def deleteRoom(listRoom):
    maPhong_delete = input("Nhập mã phòng cần xóa: ")
    found = False
    for room in listRoom:
        if room.maPhong == maPhong_delete:
            choose = int(input("Bạn có chắc chắn xóa"))
            if choose == 1:
                found = True
                listRoom.remove(room)
            else:
                print("error")
        if not found:
            print("Không tìm thấy mã phòng")


#Hàm tìm một phòng
def findRoom(listRoom):
        maPhong_find = input("Nhập mã phòng cần tìm: ")
        found = False
        for room in listRoom:
            if room.maPhong == maPhong_find:
                found = True
                print("Phòng cần tìm")
                print({room.maPhong} | {room.dayNha} | {room.dienTich} | {room.soBongDen})
        if not found:
            print("Không tìm thấy mã phòng")
    

#Hàm in danh sách các phòng
def printRoom(listRoom):
    for room in listRoom:
        print({room.maPhong} | {room.dayNha} | {room.dienTich} | {room.soBongDen})
            
    
def main():
    listRoom = []
    while True:
        print()
        print("1. thêm phòng")
        print("2. hiển thị danh sách phòng")
        print("3. tìm id phòng")
        print("4. tìm và xóa theo id phòng")
        choose = int(input("Nhập Lựa chọn: "))
        if choose == 1:
            addRoom(listRoom)
        elif choose == 2:
            printRoom(listRoom)
        elif choose == 3:
            findRoom(listRoom)
        elif choose == 4:
            deleteRoom(listRoom)
        elif choose == 5:
            updateRoom(listRoom)
        else:
            print("error")
            
main()