class SinhVien:
  def __init__(self, id, ten, gioi_tinh, tuoi, diem_toan, diem_ly, diem_hoa):
    self.id = id
    self.ten = ten
    self.gioi_tinh = gioi_tinh
    self.tuoi = tuoi
    self.diem_toan = diem_toan
    self.diem_ly = diem_ly
    self.diem_hoa = diem_hoa
    self.diem_trung_binh = self.tinh_diem_trung_binh()
    self.hoc_luc = self.xep_loai_hoc_luc()

  def tinh_diem_trung_binh(self):
    return (self.diem_toan + self.diem_ly + self.diem_hoa) / 3

  def xep_loai_hoc_luc(self):
    if self.diem_trung_binh >= 8:
      return "Giỏi"
    elif self.diem_trung_binh >= 6.5:
      return "Khá"
    elif self.diem_trung_binh >= 5:
      return "Trung Bình"
    else:
      return "Yếu"

def them_sinh_vien(danh_sach_sinh_vien):
  id_moi = 1
  if danh_sach_sinh_vien:
    id_moi = danh_sach_sinh_vien[-1].id + 1
  ten = input("Nhập tên sinh viên: ")
  gioi_tinh = input("Nhập giới tính sinh viên (nam/nữ): ")
  tuoi = int(input("Nhập tuổi sinh viên: "))
  diem_toan = float(input("Nhập điểm toán: "))
  diem_ly = float(input("Nhập điểm lý: "))
  diem_hoa = float(input("Nhập điểm hóa: "))
  sinh_vien_moi = SinhVien(id_moi, ten, gioi_tinh, tuoi, diem_toan, diem_ly, diem_hoa)
  danh_sach_sinh_vien.append(sinh_vien_moi)
  print("Thêm sinh viên thành công!")

def cap_nhat_sinh_vien(danh_sach_sinh_vien):
  id_sinh_vien = int(input("Nhập ID sinh viên cần cập nhật: "))
  tim_thay = False
  for sinh_vien in danh_sach_sinh_vien:
    if sinh_vien.id == id_sinh_vien:
      tim_thay = True
      ten_moi = input("Nhập tên mới (bỏ qua nếu không muốn đổi): ")
      if ten_moi:
        sinh_vien.ten = ten_moi
      gioi_tinh_moi = input("Nhập giới tính mới (nam/nữ, bỏ qua nếu không muốn đổi): ")
      if gioi_tinh_moi:
        sinh_vien.gioi_tinh = gioi_tinh_moi
      tuoi_moi = int(input("Nhập tuổi mới (bỏ qua nếu không muốn đổi): "))
      if tuoi_moi:
        sinh_vien.tuoi = tuoi_moi
      diem_toan_moi = float(input("Nhập điểm toán mới (bỏ qua nếu không muốn đổi): "))
      if diem_toan_moi:
        sinh_vien.diem_toan = diem_toan_moi
      diem_ly_moi = float(input("Nhập điểm lý mới (bỏ qua nếu không muốn đổi): "))
      if diem_ly_moi:
        sinh_vien.diem_ly = diem_ly_moi
      diem_hoa_moi = float(input("Nhập điểm hóa mới (bỏ qua nếu không muốn đổi): "))
      if diem_hoa_moi:
        sinh_vien.diem_hoa = diem_hoa_moi
      sinh_vien.diem_trung_binh = sinh_vien.tinh_diem_trung_binh()
      sinh_vien.hoc_luc = sinh_vien.xep_loai_hoc_luc()
      print("Cập nhật thông tin sinh viên thành công!")
      break
  if not tim_thay:
    print("Không tìm thấy sinh viên với ID:", id_sinh_vien)


def xoa_sinh_vien(danh_sach_sinh_vien):
  id_sinh_vien = int(input("Nhập ID sinh viên cần xóa: "))
  tim_thay = False
  for sinh_vien in danh_sach_sinh_vien:
    if sinh_vien.id == id_sinh_vien:
      tim_thay = True
      danh_sach_sinh_vien.remove(sinh_vien)
      print("Xóa sinh viên thành công!")
      break
  if not tim_thay:
    print("Không tìm thấy sinh viên với ID:", id_sinh_vien)

def sap_xep_sinh_vien(danh_sach_sinh_vien, tieu_chi):
  if tieu_chi == "gpa":
    danh_sach_sinh_vien.sort(key=lambda sv: sv.diem_trung_binh, reverse=True)
  elif tieu_chi == "ten":
    danh_sach_sinh_vien.sort(key=lambda sv: sv.ten)
  elif tieu_chi == "id":
    danh_sach_sinh_vien.sort(key=lambda sv: sv.id)
  else:
    print("Tiêu chí sắp xếp không hợp lệ!")
def hien_thi_danh_sach(danh_sach_sinh_vien):
  for sinh_vien in danh_sach_sinh_vien:
   print({sinh_vien.id} | {sinh_vien.ten} | {sinh_vien.diem_trung_binh} | {sinh_vien.hoc_luc})

def main():
  danh_sach_sinh_vien = []
  while True:
    print("\n--- Chương trình quản lý sinh viên ---")
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin sinh viên")
    print("3. Hiển thị danh sách sinh viên")
    print("4. Xóa sc theo id")
    # ... (các lựa chọn khác sẽ được thêm vào sau)
    lua_chon = int(input("Nhập lựa chọn của bạn: "))

    if lua_chon == 1:
      them_sinh_vien(danh_sach_sinh_vien)
    elif lua_chon == 2:
      cap_nhat_sinh_vien(danh_sach_sinh_vien)
    elif lua_chon == 3:
      hien_thi_danh_sach(danh_sach_sinh_vien)
    elif lua_chon == 4:
      xoa_sinh_vien(danh_sach_sinh_vien)
    elif lua_chon == 5:
      sap_xep_sinh_vien(danh_sach_sinh_vien, "gpa")
      hien_thi_danh_sach(danh_sach_sinh_vien)
    elif lua_chon == 6:
      sap_xep_sinh_vien(danh_sach_sinh_vien, "ten")
      hien_thi_danh_sach(danh_sach_sinh_vien)
    elif lua_chon == 7:
      sap_xep_sinh_vien(danh_sach_sinh_vien, "id")
      hien_thi_danh_sach(danh_sach_sinh_vien)
    else:
        print("Error")

main();