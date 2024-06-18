import pandas as pd

# Đọc tập dữ liệu vào DataFrame pandas
data = pd.read_csv('ten_tap_tin_du_lieu.csv')

# a. Hiển thị 5 hàng đầu tiên của tập dữ liệu
print(data.head())

# b. Hiển thị thông tin chi tiết về kiểu dữ liệu của mỗi trường
print(data.dtypes)

# c. Thực hiện thống kê mô tả về dữ liệu
print(data.describe())

# d. Chọn các cột Tiêu đề, Thể loại, Diễn viên, Đạo diễn và Xếp hạng
cot_chon = ['Tiêu đề', 'Thể loại', 'Diễn viên', 'Đạo diễn', 'Xếp hạng']
du_lieu_con = data[cot_chon]
print(du_lieu_con)

# e. Kiểm tra số lượng giá trị null cho mỗi cột
print(data.isnull().sum())

# f. Thay thế giá trị thiếu bằng giá trị trung bình, trung vị hoặc phương pháp phù hợp khác
# Thay thế giá trị thiếu trong cột 'Doanh thu' bằng giá trị trung bình của cột
data['Doanh thu'].fillna(data['Doanh thu'].mean(), inplace=True)

# g. Kiểm tra dữ liệu trùng lặp và xóa dữ liệu trùng lặp
print(data.drop_duplicates().shape)

# a. Chọn phim từ năm 2010 đến 2015, xếp hạng dưới 6.0 nhưng có doanh thu cao nhất
du_lieu_loc = data[(data['Năm'] >= 2010) & (data['Năm'] <= 2015) & (data['Xếp hạng'] < 6.0)]
phim_doanh_thu_cao_nhat = du_lieu_loc.nlargest(1, 'Doanh thu')
print(phim_doanh_thu_cao_nhat)

# b. Chọn phim thuộc thể loại "Hành động"
phim_hanh_dong = data[data['Thể loại'] == 'Hành động']
print(phim_hanh_dong)

# c. Chọn 5 phim được bình chọn nhiều nhất
top_5_phim_binh_chon = data.nlargest(5, 'Bình chọn')
print(top_5_phim_binh_chon)

# d. Tìm xếp hạng trung bình mà các đạo diễn đạt được
xep_hang_trung_binh_dao_dien = data.groupby('Đạo diễn')['Xếp hạng'].mean()
print(xep_hang_trung_binh_dao_dien)

# e. Tạo cột phân loại Xếp hạng thành "Tốt", "Trung bình" và "Kém"
data['Loại_Xếp_hạng'] = pd.cut(data['Xếp hạng'], bins=[0, 6, 7.5, 10], labels=['Kém', 'Trung bình', 'Tốt'])
print(data)

# f. Tính tổng doanh thu của phim theo Đạo diễn
doanh_thu_tong_theo_dao_dien = data.groupby('Đạo diễn')['Doanh thu'].sum()
print(doanh_thu_tong_theo_dao_dien)
