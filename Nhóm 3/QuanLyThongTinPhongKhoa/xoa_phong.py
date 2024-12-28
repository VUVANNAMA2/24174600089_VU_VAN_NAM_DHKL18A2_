def xoa_phong(danh_sach_phong):
    ma_phong = input("Nhập mã phòng cần xóa: ")
    for phong in danh_sach_phong:
        if phong['ma_phong'] == ma_phong:
            danh_sach_phong.remove(phong)
            print("Xóa phòng thành công!")
            return
    print("Không tìm thấy phòng với mã đã nhập!")