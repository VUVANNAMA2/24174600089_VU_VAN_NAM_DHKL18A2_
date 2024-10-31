#câu10
# Nhập lương của nhân viên
luong = float(input("Nhập lương của nhân viên (triệu VND): "))

# Tính thuế thu nhập và lương ròng
if luong >= 15:
    thue = 0.3 * luong
elif 7 <= luong < 15:
    thue = 0.2 * luong
else:
    thue = 0.1 * luong

luong_rong = luong - thue

# Xuất kết quả
print(f"Thuế thu nhập: {thue:.2f} triệu VND")
print(f"Lương ròng: {luong_rong:.2f} triệu VND")

