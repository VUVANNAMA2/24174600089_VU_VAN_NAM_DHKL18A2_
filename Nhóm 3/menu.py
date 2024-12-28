# # # menu.py
# # import csv
# # from QuanLyThongTinPhongKhoa import xem_phong, them_phong, sua_phong, xoa_phong, tim_kiem_phong

# # FILE_PATH = 'ds_phong_khoa.csv'

# # def hien_thi_menu():
# #     print("""
# #     === Quản Lý Phòng Khoa ===
# #     1. Xem danh sách phòng
# #     2. Thêm phòng mới
# #     3. Xóa phòng
# #     4. Chỉnh sửa thông tin phòng
# #     5. Tìm kiếm phòng
# #     6. Lưu danh sách phòng vào file
# #     7. Đọc danh sách phòng từ file
# #     0. Thoát
# #     """)

# # def menu():
# #     danh_sach_phong = []
# #     while True:
# #         hien_thi_menu()
# #         lua_chon = input("Chọn chức năng: ")
# #         if lua_chon == '1':
# #             xem_phong(danh_sach_phong)
# #         elif lua_chon == '2':
# #             them_phong(danh_sach_phong)
# #         elif lua_chon == '3':
# #             xoa_phong(danh_sach_phong)
# #         elif lua_chon == '4':
# #             sua_phong(danh_sach_phong)
# #         elif lua_chon == '5':
# #             tim_kiem_phong(danh_sach_phong)
       
            
# #         elif lua_chon == '0':
# #             print("Thoát chương trình.")
# #             break
# #         else:
# #             print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

# # if __name__ == "_menu_":
# #     menu()
# from QuanLyThongTinPhongKhoa import xem_phong, them_phong, sua_phong, xoa_phong, tim_kiem_phong

# def menu_phong_khoa():
#     """Hiển thị menu quản lý Thông Tin phòng khoa."""
#     while True:
#         print("\n--- Quản Lý Thông Tin Phòng Khoa ---")
#         print("1. Xem danh sách phòng")
#         print("2. Thêm phòng")
#         print("3. Sửa phòng")
#         print("4. Xóa phòng")
#         print("5. Tìm kiếm phòng")
#         print("0. Quay lại menu chính")
#         try:
#             choice = int(input("Chọn chức năng: "))
#             if choice == 1:
#                 xem_phong.xem_danh_sach_phong()
#             elif choice == 2:
#                 ma_phong = input("Nhập mã phòng: ").strip()
#                 ten_phong = input("Nhập tên phòng: ").strip()
#                 loai_phong = int(input("Nhập loại phòng (0, 1, 2): ").strip())
#                 vi_tri_khu_nha = int(input("Nhập vị trí khu nhà (0-5): ").strip())
#                 vi_tri_tang = int(input("Nhập vị trí tầng: ").strip())
#                 sdt_quan_ly = input("Nhập số điện thoại quản lý: ").strip()
#                 ma_khoa = input("Nhập mã khoa: ").strip()

#                 phong_moi = {
#                     "MaPhong": ma_phong,
#                     "TenPhong": ten_phong,
#                     "LoaiPhong": loai_phong,
#                     "ViTriKhuNha": vi_tri_khu_nha,
#                     "ViTriTang": vi_tri_tang,
#                     "SDTQuanLy": sdt_quan_ly,
#                     "MaKhoa": ma_khoa,
#                 }
#                 them_phong.them_phong(phong_moi)
#             elif choice == 3:
#                 ma_phong = input("Nhập mã phòng cần sửa: ").strip()
#                 print("Nhập các thông tin mới (để trống nếu không muốn thay đổi):")
#                 ten_phong = input("Tên phòng: ").strip()
#                 loai_phong = input("Loại phòng (0, 1, 2): ").strip()
#                 vi_tri_khu_nha = input("Vị trí khu nhà (0-5): ").strip()
#                 vi_tri_tang = input("Vị trí tầng: ").strip()
#                 sdt_quan_ly = input("Số điện thoại quản lý: ").strip()
#                 ma_khoa = input("Mã khoa: ").strip()

#                 thong_tin_moi = {}
#                 if ten_phong:
#                     thong_tin_moi["TenPhong"] = ten_phong
#                 if loai_phong:
#                     thong_tin_moi["LoaiPhong"] = int(loai_phong)
#                 if vi_tri_khu_nha:
#                     thong_tin_moi["ViTriKhuNha"] = int(vi_tri_khu_nha)
#                 if vi_tri_tang:
#                     thong_tin_moi["ViTriTang"] = int(vi_tri_tang)
#                 if sdt_quan_ly:
#                     thong_tin_moi["SDTQuanLy"] = sdt_quan_ly
#                 if ma_khoa:
#                     thong_tin_moi["MaKhoa"] = ma_khoa

#                 sua_phong.sua_phong(ma_phong, thong_tin_moi)
#             elif choice == 4:
#                 ma_phong = input("Nhập mã phòng cần xóa: ").strip()
#                 xoa_phong.xoa_phong(ma_phong)
#             elif choice == 5:
#                 ma_phong = input("Nhập mã phòng cần tìm: ").strip()
#                 tim_kiem_phong.tim_kiem_phong(ma_phong)
#             elif choice == 0:
#                 break
#             else:
#                 print("Vui lòng chọn số hợp lệ.")
#         except ValueError:
#             print("Lỗi: Vui lòng nhập một số hợp lệ.")
# if __name__ == "__main__":
#       menu

# def menu_phong_khoa():
#     """Hiển thị menu quản lý Thông Tin phòng khoa."""
#     while True:
#         print("\n--- Quản Lý Thông Tin Phòng Khoa ---")
#         print("1. Xem danh sách phòng")
#         print("2. Thêm phòng")
#         print("3. Sửa phòng")
#         print("4. Xóa phòng")
#         print("5. Tìm kiếm phòng")
#         print("0. Quay lại menu chính")
#         try:
#             choice = int(input("Chọn chức năng: "))
#             if choice == 1:
#                 xem_phong.xem_danh_sach_phong()
#             elif choice == 2:
#                 ma_phong = input("Nhập mã phòng: ").strip()
#                 ten_phong = input("Nhập tên phòng: ").strip()
#                 loai_phong = int(input("Nhập loại phòng (0, 1, 2): ").strip())
#                 vi_tri_khu_nha = int(input("Nhập vị trí khu nhà (0-5): ").strip())
#                 vi_tri_tang = int(input("Nhập vị trí tầng: ").strip())
#                 sdt_quan_ly = input("Nhập số điện thoại quản lý: ").strip()
#                 ma_khoa = input("Nhập mã khoa: ").strip()

#                 phong_moi = {
#                     "MaPhong": ma_phong,
#                     "TenPhong": ten_phong,
#                     "LoaiPhong": loai_phong,
#                     "ViTriKhuNha": vi_tri_khu_nha,
#                     "ViTriTang": vi_tri_tang,
#                     "SDTQuanLy": sdt_quan_ly,
#                     "MaKhoa": ma_khoa,
#                 }
#                 them_phong.them_phong(phong_moi)
#             elif choice == 3:
#                 ma_phong = input("Nhập mã phòng cần sửa: ").strip()
#                 print("Nhập các thông tin mới (để trống nếu không muốn thay đổi):")
#                 ten_phong = input("Tên phòng: ").strip()
#                 loai_phong = input("Loại phòng (0, 1, 2): ").strip()
#                 vi_tri_khu_nha = input("Vị trí khu nhà (0-5): ").strip()
#                 vi_tri_tang = input("Vị trí tầng: ").strip()
#                 sdt_quan_ly = input("Số điện thoại quản lý: ").strip()
#                 ma_khoa = input("Mã khoa: ").strip()

#                 thong_tin_moi = {}
#                 if ten_phong:
#                     thong_tin_moi["TenPhong"] = ten_phong
#                 if loai_phong:
#                     thong_tin_moi["LoaiPhong"] = int(loai_phong)
#                 if vi_tri_khu_nha:
#                     thong_tin_moi["ViTriKhuNha"] = int(vi_tri_khu_nha)
#                 if vi_tri_tang:
#                     thong_tin_moi["ViTriTang"] = int(vi_tri_tang)
#                 if sdt_quan_ly:
#                     thong_tin_moi["SDTQuanLy"] = sdt_quan_ly
#                 if ma_khoa:
#                     thong_tin_moi["MaKhoa"] = ma_khoa

#                 sua_phong.sua_phong(ma_phong, thong_tin_moi)
#             elif choice == 4:
#                 ma_phong = input("Nhập mã phòng cần xóa: ").strip()
#                 xoa_phong.xoa_phong(ma_phong)
#             elif choice == 5:
#                 ma_phong = input("Nhập mã phòng cần tìm: ").strip()
#                 tim_kiem_phong.tim_kiem_phong(ma_phong)
#             elif choice == 0:
#                 break
#             else:
#                 print("Vui lòng chọn số hợp lệ.")
#         except ValueError:
#             print("Lỗi: Vui lòng nhập một số hợp lệ.")

#             print("Lựa chọn không hợp lệ. Vui lòng thử lại."

import libs.ds_phong_Khoa as xl
ds_phong_Khoa = []
while True:
    print(" Quản Lý Thông Tin Phòng Khoa: ")
    print("1. xem phòng")
    print("2. thêm phòng")
    print("3. sửa phòng")
    print("4. xóa phòng")
    print("5. tìm kiếm phòng")
    print("6. file_utils.py")
    print("0. thoát")
try:
    lua_chon = int(input("Nhap lua chon: "))
except:
    print("Yeu cau nhap so!")
else:
    if lua_chon == 1:
        print("xem phong")
        xl.xem_phong(ds_phong_Khoa)
    elif lua_chon == 2:
        print("them phong")
        xl.them_phong(ds_phong_Khoa)
    elif lua_chon == 3:
        print("sua phong")
        xl.sua_phong(ds_phong_Khoa)
    elif lua_chon == 4:
        print("xoa phong")
        xl.xoa_phong(ds_phong_Khoa)
    elif lua_chon == 5:
        print("tim kiem phong")
        xl.tim_kiem_phong(ds_phong_Khoa)
    elif lua_chon == 6:
        print("file_utils")
        xl.file_utils(ds_phong_Khoa)
    elif lua_chon == 0:
        print("Thoát chương trình. Tạm biêtyj!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")