class GiaoDich:
  def __init__(self, ma_gd, ngay_gd, don_gia, so_luong):
    self.ma_gd = ma_gd
    self.ngay_gd = ngay_gd
    self.don_gia = don_gia
    self.so_luong = so_luong

class GiaoDichVang(GiaoDich):
  def __init__(self, ma_gd, ngay_gd, don_gia, so_luong, loai_vang):
    super().__init__(ma_gd, ngay_gd, don_gia, so_luong)
    self.loai_vang = loai_vang

  def tinh_thanh_tien(self):
    return self.so_luong * self.don_gia

class GiaoDichTienTe(GiaoDich):
  def __init__(self, ma_gd, ngay_gd, don_gia, so_luong, ti_gia, loai_tien_te):
    super().__init__(ma_gd, ngay_gd, don_gia, so_luong)
    self.ti_gia = ti_gia
    self.loai_tien_te = loai_tien_te

  def tinh_thanh_tien(self):
    if self.loai_tien_te == "USD" or self.loai_tien_te == "EUR":
      return self.so_luong * self.don_gia * self.ti_gia
    else:
      return self.so_luong * self.don_gia

# Khởi tạo dữ liệu giao dịch
giao_dich_vang = []
giao_dich_tien_te = []

# Giao dịch vàng
giao_dich_vang.append(GiaoDichVang("GDV1", "2023-12-31", 5000000, 10, "SJC"))
giao_dich_vang.append(GiaoDichVang("GDV2", "2024-01-01", 5200000, 12, "24K"))
giao_dich_vang.append(GiaoDichVang("GDV3", "2024-01-02", 5300000, 15, "9999"))

# Giao dịch tiền tệ
giao_dich_tien_te.append(GiaoDichTienTe("GDT1", "2023-12-31", 23000, 100, 23000, "USD"))
giao_dich_tien_te.append(GiaoDichTienTe("GDT2", "2024-01-01", 24000, 150, 24000, "EUR"))
giao_dich_tien_te.append(GiaoDichTienTe("GDT3", "2024-01-02", 25000, 200, 25000, "VND"))

# Tính tổng số lượng cho từng loại giao dịch
tong_so_luong_vang = sum(giao_dich.so_luong for giao_dich in giao_dich_vang)
tong_so_luong_tien_te = sum(giao_dich.so_luong for giao_dich in giao_dich_tien_te)

# Tính trung bình thành tiền của giao dịch tiền tệ
tong_thanh_tien_tien_te = sum(giao_dich.tinh_thanh_tien() for giao_dich in giao_dich_tien_te)
trung_binh_thanh_tien_tien_te = tong_thanh_tien_tien_te / len(giao_dich_tien_te)

# Xuất giao dịch có đơn giá > 1 tỷ
giao_dich_don_gia_cao = []
for giao_dich in giao_dich_vang + giao_dich_tien_te:
  if giao_dich.don_gia > 1000000000:
    giao_dich_don_gia_cao.append(giao_dich)

print("## Danh sách giao dịch vàng:")
for giao_dich in giao_dich_vang:
  print(f"- {giao_dich.__dict__}")

