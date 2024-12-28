# from .file_utils import doc_danh_sach_phong, ghi_danh_sach_phong

# def sua_phong(danh_sach_phong):
#     ma_phong = input("Nhập mã phòng cần chỉnh sửa: ")
#     for phong in danh_sach_phong:
#         if phong['ma_phong'] == ma_phong:
#             phong['ten_phong'] = input("Nhập tên phòng mới: ")
#             phong['khoa'] = input("Nhập khoa mới: ")
#             print("Cập nhật thông tin phòng thành công!")
#             return
#     print("Không tìm thấy phòng với mã đã nhập!")
from .file_utils import doc_danh_sach_phong, ghi_danh_sach_phong

def sua_phong(ma_phong, thong_tin_moi):
    danh_sach = doc_danh_sach_phong()
    for phong in danh_sach:
        if phong["MaPhong"] == ma_phong:
            phong.update(thong_tin_moi)
            break
    ghi_danh_sach_phong(danh_sach)
    print(f"Sửa thông tin phòng có mã {ma_phong} thành công!")