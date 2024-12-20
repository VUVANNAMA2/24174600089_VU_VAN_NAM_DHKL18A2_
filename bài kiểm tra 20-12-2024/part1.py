# Viết chương trình quản lý đội bóng với mỗi cầu thủ 
# Hàm tính thưởng dựa trên số huy chương
def tinh_thuong(so_huy_chuong):
    if so_huy_chuong > 10:
        return so_huy_chuong * 500000
    elif 5 <= so_huy_chuong < 10:
        return so_huy_chuong * 300000
    elif 1 <= so_huy_chuong < 5:
        return so_huy_chuong * 200000
    else:
        return 0

# Hàm nhập thông tin cầu thủ từ bàn phím
def nhap_cau_thu():
    try:
        ma_cau_thu = input("Nhập mã cầu thủ: ")
        ten_cau_thu = input("Nhập tên cầu thủ: ")
        tuoi = int(input("Nhập tuổi cầu thủ: "))
        assert tuoi > 0, "Tuổi phải là số nguyên dương!"
        vi_tri = input("Nhập vị trí (thủ môn/hậu vệ/tiền vệ/tiền đạo): ").lower()
        assert vi_tri in ["thủ môn", "hậu vệ", "tiền vệ", "tiền đạo"], "Vị trí không hợp lệ!"
        so_huy_chuong = int(input("Nhập số huy chương: "))
        assert so_huy_chuong >= 0, "Số huy chương không được âm!"
    except ValueError:
        print("Lỗi: Nhập dữ liệu không hợp lệ!")
        return None
    except AssertionError as e:
        print(f"Lỗi: {e}")
        return None
    else:
        thuong = tinh_thuong(so_huy_chuong)
        return [ma_cau_thu, ten_cau_thu, tuoi, vi_tri, so_huy_chuong, thuong]

# Hàm hiển thị danh sách cầu thủ
def hien_thi_danh_sach(danh_sach):
    if not danh_sach:
        print("\nDanh sách cầu thủ trống!")
    else:
        print("\n===== Danh sách cầu thủ =====")
        for cau_thu in danh_sach:
            print(f"\nMã cầu thủ: {cau_thu[0]}")
            print(f"Tên cầu thủ: {cau_thu[1]}")
            print(f"Tuổi: {cau_thu[2]}")
            print(f"Vị trí: {cau_thu[3]}")
            print(f"Số huy chương: {cau_thu[4]}")
            print(f"Thưởng: {cau_thu[5]:,} đồng")
       
# Hàm tìm kiếm cầu thủ theo mã
def tim_kiem_cau_thu(danh_sach, ma_cau_thu):
    for cau_thu in danh_sach:
        if cau_thu[0] == ma_cau_thu:
            return cau_thu
    return None

 # Hàm xóa cầu thủ theo mã
def xoa_cau_thu(danh_sach):
    ma_cau_thu = input("Nhập mã cầu thủ cần xóa: ")
    cau_thu = tim_kiem_cau_thu(danh_sach, ma_cau_thu)
    if cau_thu:
        danh_sach.remove(cau_thu)
        print("Xóa cầu thủ thành công!")
    else:
        print("Không tìm thấy cầu thủ!")

# Hàm sửa thông tin cầu thủ theo mã
def sua_cau_thu(danh_sach):
    ma_cau_thu = input("Nhập mã cầu thủ cần sửa: ")
    cau_thu = tim_kiem_cau_thu(danh_sach, ma_cau_thu)
    if cau_thu:
        try:
            cau_thu[1] = input("Nhập tên mới: ")
            cau_thu[2] = int(input("Nhập tuổi mới: "))
            assert cau_thu[2] > 0, "Tuổi phải là số nguyên dương!"
            cau_thu[3] = input("Nhập vị trí mới: ").lower()
            assert cau_thu[3] in ["thủ môn", "hậu vệ", "tiền vệ", "tiền đạo"], "Vị trí không hợp lệ!"
            cau_thu[4] = int(input("Nhập số huy chương mới: "))
            assert cau_thu[4] >= 0, "Số huy chương không được âm!"
        except ValueError:
            print("Lỗi: Nhập dữ liệu không hợp lệ!")
        except AssertionError as e:
            print(f"Lỗi: {e}")
        else:
            cau_thu[5] = tinh_thuong(cau_thu[4])  # Cập nhật lại thưởng
            print("Sửa thông tin cầu thủ thành công!")
    else:
        print("Không tìm thấy cầu thủ!")

# Hàm sắp xếp danh sách cầu thủ theo số huy chương
def sap_xep_theo_huy_chuong(danh_sach):
    for i in range(len(danh_sach)):
        for j in range(i + 1, len(danh_sach)):
            if danh_sach[i][4] > danh_sach[j][4]:  # So sánh số huy chương
                danh_sach[i], danh_sach[j] = danh_sach[j], danh_sach[i]
    print("Danh sách cầu thủ đã được sắp xếp theo số huy chương.")

# Hàm chính
def main():
    danh_sach_cau_thu = []

    while True:
        print("\n===== Quản lý đội bóng =====")
        print("1. Xem danh sách cầu thủ")
        print("2. Nhập cầu thủ mới")
        print("3. Tìm kiếm và xóa cầu thủ")
        print("4. Tìm kiếm và sửa cầu thủ")
        print("5. Sắp xếp cầu thủ theo số huy chương")
        print("6. Thoát")
        lua_chon = input("Nhập lựa chọn (1-6): ")

        try:
            assert lua_chon in ["1", "2", "3", "4", "5", "6"], "Lựa chọn không hợp lệ!"
        except AssertionError as e:
            print(f"Lỗi: {e}")
        else:
            if lua_chon == "1":
                hien_thi_danh_sach(danh_sach_cau_thu)
            elif lua_chon == "2":
                cau_thu = nhap_cau_thu()
                if cau_thu:
                    danh_sach_cau_thu.append(cau_thu)
                    print("Thêm cầu thủ thành công!")
            elif lua_chon == "3":
                xoa_cau_thu(danh_sach_cau_thu)
            elif lua_chon == "4":
                sua_cau_thu(danh_sach_cau_thu)
            elif lua_chon == "5":
                sap_xep_theo_huy_chuong(danh_sach_cau_thu)
                hien_thi_danh_sach(danh_sach_cau_thu)
            elif lua_chon == "6":
                print("Thoát chương trình!")
                break

if __name__ == "_main_":
    main()   