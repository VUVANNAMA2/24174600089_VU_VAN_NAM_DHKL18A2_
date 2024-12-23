def xem_danh_sach(danh_sach):
    if not danh_sach:
        print("Danh sách phòng trống.")
        return
    print("Danh sách phòng:")
    for phong in danh_sach:
         print(f"Mã phòng: {phong['ma_phong']}, Tên phòng: {phong['ten_phong']}, Loại phòng: {phong['loai_phong']}, "
              f"Vị trí khu: {phong['vi_tri_khu']}, Vị trí tầng: {phong['vi_tri_tang']}, SĐT quản lý: {phong['sdt_quan_ly']}, "
              f"Mã khoa: {phong['ma_khoa']}")