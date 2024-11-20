# Nhập chuỗi từ người dùng
chuoi_nhap = input("Nhap vao chuoi ky tu: ")

chu_so = 0
chu_cai = 0
ky_tu_dac_biet = 0

for chu in chuoi_nhap:
    if chu.isdigit():# isdigit kiểm tra chuỗi có phải toàn bộ là số không
        chu_so =chu_so + 1
    elif chu.isalpha():#isalpha kiểm tta chuỗi có phải lf chữ cái không
        chu_cai =  chu_cai + 1
    else:
        ky_tu_dac_biet =ky_tu_dac_biet + 1

print(f"So ky tu la chu: {chu_cai}")
print(f"So ky tu la so: {chu_so}")
print(f"So ky tu dac biet: {ky_tu_dac_biet}")
