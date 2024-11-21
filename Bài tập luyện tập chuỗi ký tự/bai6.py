nhap_vao_chuoi = input("nhap vao ky tu:")
if nhap_vao_chuoi.startswith('-') and chuoi_nhap[1:].isdigit(): #starswith lệnh kiểm tra số gì "-"(la số âm)   isdigit kiểm tra xem là số hay k
    print(" chuoi la so am")
else:
    print(" chuoi khong phai so am")

#bài 7  Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải số thập phân hay không
nhap_vao_chuoi = input("nhap vao ky tu:")
if nhap_vao_chuoi.isdecimal() and  nhap_vao_chuoi.isdigit():    #isdecimal kiểm tra xem số thập phân hay không isdigit kiểm tra phải là só hay k
             print(nhap_vao_chuoi.isdecimal())
             print("chuoi la so thap phan") #true
else:
         print(" chuoi la so thap phan")     #false     