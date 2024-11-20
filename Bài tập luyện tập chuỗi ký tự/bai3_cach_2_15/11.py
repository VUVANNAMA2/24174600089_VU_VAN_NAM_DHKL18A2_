# Nhập vào một chuỗi từ người dùng
chuoi = input("Nhập vào một chuỗi bất kỳ: ")

# Biến để lưu chuỗi kết quả
chuoi_sau_khi_xoa = ""

# Biến để theo dõi khoảng trắng thừa
trong_khoang_trong = False

# Lặp qua từng ký tự trong chuỗi
for char in chuoi:
    if char != " ":  # Nếu ký tự không phải là khoảng trắng
        chuoi_sau_khi_xoa += char
        trong_khoang_trong = False
    elif not trong_khoang_trong:  # Nếu ký tự là khoảng trắng và chưa gặp khoảng trắng trước đó
        chuoi_sau_khi_xoa += " "
        trong_khoang_trong = True

# Loại bỏ khoảng trắng ở đầu và cuối chuỗi
if chuoi_sau_khi_xoa and chuoi_sau_khi_xoa[0] == " ":
    chuoi_sau_khi_xoa = chuoi_sau_khi_xoa[1:]
if chuoi_sau_khi_xoa and chuoi_sau_khi_xoa[-1] == " ":
    chuoi_sau_khi_xoa = chuoi_sau_khi_xoa[:-1]

# In chuỗi đã xử lý
print("Chuỗi sau khi xóa khoảng trống thừa:", chuoi_sau_khi_xoa)
