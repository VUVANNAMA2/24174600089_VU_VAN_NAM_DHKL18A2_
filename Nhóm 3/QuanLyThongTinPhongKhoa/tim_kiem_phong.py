def tim_kiem_phong(danh_sach_phong):
    tu_khoa = input("Nhập từ khóa tìm kiếm: ")
    ket_qua = [phong for phong in danh_sach_phong if tu_khoa.lower() in phong['ten_phong'].lower()]
    if ket_qua:
        for phong in ket_qua:
            print(f"Mã phòng: {phong['ma_phong']}, Tên phòng: {phong['ten_phong']}, Khoa: {phong['khoa']}")
    else:
        print("Không tìm thấy phòng nào phù hợp!")

