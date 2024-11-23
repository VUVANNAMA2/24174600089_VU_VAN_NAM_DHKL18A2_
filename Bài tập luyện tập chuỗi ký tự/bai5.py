nhap_vao_chuoi = input("nhap vao chuoi ky tu")
viet_hoa=0
viet_thuong=0
for chu in nhap_vao_chuoi:
    if chu.isupper():# isupper kiểm tra chữ hoa
       viet_hoa=viet_hoa+1
    elif chu.islower():#islower kiểm tra chữ cái in thường
        viet_thuong=viet_thuong+1
print(f"chu cai in hoa: {viet_hoa}")  
print(f"chu cai in thuong: {viet_thuong}")   
