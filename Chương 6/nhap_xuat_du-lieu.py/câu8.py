# Hàm để tính loại điểm
def xep_loai(diem_trung_binh):
    if diem_trung_binh >= 9:
        return 'A'
    elif diem_trung_binh >= 7:
        return 'B'
    elif diem_trung_binh >= 5:
        return 'C'
    else:
        return 'D'

# Nhập điểm từ người dùng
diem_chuyen_can = float(input("Nhập điểm chuyên cần: "))
diem_giua_ky = float(input("Nhập điểm giữa kỳ: "))
diem_cuoi_ky = float(input("Nhập điểm cuối kỳ: "))

# Tính điểm trung bình
diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky) / 3

# Xếp loại
loai_diem = xep_loai(diem_trung_binh)

# Xuất kết quả
print(f"Điểm trung bình: {diem_trung_binh:.2f}")
print(f"Xếp loại: {loai_diem}")

